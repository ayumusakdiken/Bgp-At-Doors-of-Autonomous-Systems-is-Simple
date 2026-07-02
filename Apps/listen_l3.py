import socket
import struct

# Ethernet ve IPv4 sabitleri
ETH_P_ALL = 0x0003  # bütün protokolleri yakalamak için kullanılan sabit değer
ETH_HEADER_LEN = 14  # Ethernet başlığı uzunluğu

# IPv4 başlık çözümleme fonksiyonu
def ip_header_decapsulation(ip_header):
	version_ihl = ip_header[0]  # IP başlığının ilk baytı, sürüm ve IHL (Internet Header Length) bilgisini içerir
	version = version_ihl >> 4  # Sürüm bilgisi, ilk 4 bitten elde edilir
	ihl = version_ihl & 0x0F  # IHL bilgisi, son 4 bitten elde edilir
	tos = ip_header[1]  # Type of Service (Hizmet Türü)
	total_length = struct.unpack('!H', ip_header[2:4])[0]  # Toplam uzunluk, ağ bayt sırasına göre (big-endian) bir tamsayıya dönüştürülür
	identification = struct.unpack('!H', ip_header[4:6])[0]  # Tanımlayıcı (Identification)
	flags_fragment_offset = struct.unpack('!H', ip_header[6:8])[0]  # Bayraklar ve fragment offset
	ttl = ip_header[8]  # Time to Live (Yaşam Süresi)
	protocol = ip_header[9]  # Protokol
	header_checksum = struct.unpack('!H', ip_header[10:12])[0]  # Başlık kontrol toplamı (checksum)
	src_ip = socket.inet_ntoa(ip_header[12:16])  # Kaynak IP adresi, baytlardan string formatına dönüştürülür
	dst_ip = socket.inet_ntoa(ip_header[16:20])  # Hedef IP adresi, baytlardan string formatına dönüştürülür

	return {
		'version': version,
		'ihl': ihl,
		'tos': tos,
		'total_length': total_length,
		'identification': identification,
		'flags_fragment_offset': flags_fragment_offset,
		'ttl': ttl,
		'protocol': protocol,
		'header_checksum': header_checksum,
		'src_ip': src_ip,
		'dst_ip': dst_ip
	}

# Ana fonksiyon
def main():
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))  # Ham soket oluşturur ve tüm protokolleri yakalamak için ETH_P_ALL kullanır
	conn.bind(('eth0', 0))  # 'eth0' yerine uygun ağ arayüzünü kullanın

	while True:
		frame, addr = conn.recvfrom(65535)  # Soketten gelen çerçeveyi alır
		if len(frame) < ETH_HEADER_LEN + 20:  # Ethernet başlığı ve minimum IP başlığı uzunluğu kontrolü
			continue  # Yetersiz uzunlukta çerçeveleri atla

		eth_type = struct.unpack('!H', frame[12:14])[0]  # Ethernet tipini çerçeveden çıkarır
		if eth_type != 0x0800:  # Sadece IPv4 paketlerini işleme al
			continue

		ip_header = frame[ETH_HEADER_LEN:ETH_HEADER_LEN + 20]  # IP başlığını çıkarır
		ip_info = ip_header_decapsulation(ip_header)  # IP başlığını çözümle

		print(f"Received IPv4 packet: {ip_info}")
	
if __name__ == "__main__":
	main()  # main fonksiyonunu çalıştırır
