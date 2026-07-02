import socket
import struct

# Ethernet başlığı oluşturmak
def create_eth_header(dst_mac, src_mac, eth_type):
	dst_mac_bytes = bytes.fromhex(dst_mac.replace(':', ''))  # Hedef MAC adresini baytlara dönüştürür
	src_mac_bytes = bytes.fromhex(src_mac.replace(':', ''))  # Kaynak MAC adresini baytlara dönüştürür
	eth_type_bytes = struct.pack('!H', eth_type)  # Ethernet tipini ağ bayt sırasına göre (big-endian) baytlara dönüştürür
	return dst_mac_bytes + src_mac_bytes + eth_type_bytes  # Ethernet başlığını birleştirir ve döndürür

# IP başlığı oluşturmak
def create_ip_header(src_ip, dst_ip, payload_len):
	version_ihl = (4 << 4) + 5  # IPv4 ve IHL (Internet Header Length). IHL değeri 5, yani 20 baytlık bir başlık uzunluğunu temsil eder.
	tos = 0  # Type of Service (Hizmet Türü)
	total_length = 20 + payload_len  # Toplam uzunluk, IP başlığı (20 bayt) ve yük uzunluğunun toplamıdır.
	identification = 54321  # Tanımlayıcı (Identification)
	flags_fragment_offset = 0  # Bayraklar ve fragment offset
	ttl = 64  # Time to Live (Yaşam Süresi)
	protocol = 6  # Protokol (TCP için 6)
	header_checksum = 0  # Başlık kontrol toplamı (checksum), daha sonra hesaplanacak
	src_ip_bytes = socket.inet_aton(src_ip)  # Kaynak IP adresini baytlara dönüştürür
	dst_ip_bytes = socket.inet_aton(dst_ip)  # Hedef IP adresini baytlara dönüştürür
	ip_header = struct.pack('!BBHHHBBH4s4s', version_ihl, tos, total_length, identification, flags_fragment_offset, ttl, protocol, header_checksum, src_ip_bytes, dst_ip_bytes)  # IP başlığını paketler
	return ip_header  # IP başlığını döndürür

# Ham soket oluşturmak ve çerçeveyi göndermek
def send_frame(dst_mac, src_mac, src_ip, dst_ip, payload):
	eth_type = 0x0800  # IP protokolü için Ethernet tipi
	eth_header = create_eth_header(dst_mac, src_mac, eth_type)  # Ethernet başlığını oluşturur
	payload_len = len(payload)  # Yük uzunluğunu hesaplar
	ip_header = create_ip_header(src_ip, dst_ip, payload_len)  # IP başlığını oluşturur
	frame = eth_header + ip_header + payload  # Ethernet başlığı, IP başlığı ve yükü birleştirir

	# Ham soket oluşturur ve çerçeveyi gönderir
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)  # Ham soket oluşturur
	conn.bind(('eth0', 0))  # 'eth0' yerine uygun ağ arayüzünü kullanın
	conn.send(frame)  # Çerçeveyi gönderir
	conn.close()  # Soketi kapatı
	
	print(f"Frame sent successfully!")
	print(f"Frame: {frame.hex()}")  # Gönderilen çerçevenin hex formatında çıktısını verir


def main():
	dst_mac = 'ff:ff:ff:ff:ff:ff'  # Hedef MAC adresi (broadcast)
	src_mac = '00:0a:95:9d:68:16'  # Kaynak MAC adresi
	src_ip = '192.168.1.100'  # Kaynak IP adresi
	dst_ip = '192.168.1.1'  # Hedef IP adresi
	payload = b'Hello, World!'  # Gönderilecek veri

	send_frame(dst_mac, src_mac, src_ip, dst_ip, payload)

if __name__ == "__main__":
	main()  # main fonksiyonunu çalıştırır
