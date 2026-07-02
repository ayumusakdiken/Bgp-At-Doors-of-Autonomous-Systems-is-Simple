import socket
import struct

# Ethernet başlığı decode etmek
def decode_eth_header(frame):
	eth_header = frame[:14]  # Ethernet başlığı ilk 14 bayttır
	dst_mac, src_mac, eth_type = struct.unpack('!6s6sH', eth_header)  # Ethernet başlığını unpack eder
	dst_mac_str = ':'.join(format(b, '02x') for b in dst_mac)  # Hedef MAC adresini string formatına çevirir
	src_mac_str = ':'.join(format(b, '02x') for b in src_mac)  # Kaynak MAC adresini string formatına çevirir
	return dst_mac_str, src_mac_str, eth_type  # Hedef MAC, kaynak MAC ve Ethernet tipini döndürür

# IP başlığı decode etmek
def decode_ip_header(frame):
	ip_header = frame[14:34]  # IP başlığı Ethernet başlığından sonra gelir ve 20 bayttır
	version_ihl, tos, total_length, identification, flags_fragment_offset, ttl, protocol, header_checksum, src_ip_bytes, dst_ip_bytes = struct.unpack('!BBHHHBBH4s4s', ip_header)  # IP başlığını unpack eder
	src_ip_str = socket.inet_ntoa(src_ip_bytes)  # Kaynak IP adresini string formatına çevirir
	dst_ip_str = socket.inet_ntoa(dst_ip_bytes)  # Hedef IP adresini string formatına çevirir
	return src_ip_str, dst_ip_str, protocol  # Kaynak IP, hedef IP ve protokolü döndürür

# TCP başlığı decode etmek
def decode_tcp_header(frame):
	tcp_header = frame[34:54]  # TCP başlığı IP başlığından sonra gelir ve 20 bayttır
	src_port, dst_port, seq_num, ack_num, data_offset_reserved_flags, window_size, tcp_checksum, urgent_pointer = struct.unpack('!HHLLBBHHH', tcp_header)  # TCP başlığını unpack eder
	return src_port, dst_port, seq_num, ack_num  # Kaynak port, hedef port, sıralama numarası ve onay numarasını döndürür

# Ham soket oluşturmak ve çerçeveyi dinlemek
def listen_frame():
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))  # Ham soket oluşturur
	while True:
		frame, addr = conn.recvfrom(65535)  # Çerçeveyi alır
		dst_mac, src_mac, eth_type = decode_eth_header(frame)  # Ethernet başlığını decode eder
		src_ip, dst_ip, protocol = decode_ip_header(frame)  # IP başlığını decode eder
		src_port, dst_port, seq_num, ack_num = decode_tcp_header(frame)  # TCP başlığını decode eder

		print(f"Received frame:")
		print(f"Destination MAC: {dst_mac}, Source MAC: {src_mac}, Eth Type: {eth_type}")
		print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")
		print(f"Source Port: {src_port}, Destination Port: {dst_port}, Seq Num: {seq_num}, Ack Num: {ack_num}")
		print("-" * 50)

if __name__ == "__main__":
	listen_frame()  # listen_frame fonksiyonunu çalıştırır
