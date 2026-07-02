import socket
import struct

# Ethernet frame header format
ETH_P_ALL = 0x0003  # bütün protokolleri yakalamak için kullanılan sabit değer

# ethernet frame decapsulation yapar
def eth_frame_decapsulation(frame):
	dst_mac = frame[0:6] # Hedef MAC adresini çerçeveden çıkarır
	src_mac = frame[6:12] # Kaynak MAC adresini çerçeveden çıkarır
	eth_type = struct.unpack('!H', frame[12:14])[0] # Ethernet tipini çerçeveden çıkarır ve ağ bayt sırasına göre (big-endian) bir tamsayıya dönüştürür
	payload = frame[14:] # Çerçevenin geri kalan kısmını (yük) çıkarır
	return dst_mac, src_mac, eth_type, payload

def main():
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL)) # Ham soket oluşturur ve tüm protokolleri yakalamak için ETH_P_ALL kullanır
	conn.bind(('eth0', 0))  # 'eth0' yerine uygun ağ arayüzünü kullanın, eth0 genellikle Linux sistemlerinde varsayılan ağ arayüzüdür.

	while True:
		frame, addr = conn.recvfrom(65535)  # Soketten gelen çerçeveyi alır, 65535
		dst_mac, src_mac, eth_type, payload = eth_frame_decapsulation(frame)  # Çerçeveyi çözümleyerek hedef MAC, kaynak MAC, Ethernet tipi ve yükü çıkarır
		print(f"Received frame: dst_mac={dst_mac}, src_mac={src_mac}, eth_type={eth_type}, payload={payload}")

if __name__ == "__main__":
	main()  # main fonksiyonunu çalıştırır
