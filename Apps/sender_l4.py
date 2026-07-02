import socket
import struct

# Ethernet başlığı oluşturmak
def create_eth_header(dst_mac, src_mac, eth_type):
    return struct.pack("!6s6sH", dst_mac, src_mac, eth_type)

# IP başlığı oluşturmak
def create_ip_header(src_ip, dst_ip, payload_len):
	version_ihl = (4 << 4) + 5  # IPv4 ve IHL (Internet Header Length)
	tos = 0  # Type of Service, 0 = normal service, 1 = minimize delay, 2 = maximize throughput, 4 = maximize reliability
	total_length = 20 + payload_len  # Toplam uzunluk. +20 çünkü IP başlığı 20 bayttır; src_ip ve dst_ip 4 bayt, payload_len ise yük uzunluğunu temsil eder.
	identification = 54321  # Tanımlayıcı, her paketin benzersiz bir şekilde tanımlanmasını sağlar. Bu örnekte sabit bir değer kullanılmıştır.
	flags_fragment_offset = 0  # Bayraklar ve fragment offset, 0 = don't fragment, 1 = more fragments, 2 = reserved
	ttl = 64  # Time to Live, 64, paketin ağda ne kadar süre kalacağını belirler. Her yönlendirici (router) paketi işlerken bu değeri azaltır ve 0 olduğunda paket düşürülür.
	protocol = 6  # Protokol (TCP için), 6, UDP için 17, ICMP için 1 gibi değerler alabilir.
	header_checksum = 0  # Başlık kontrol toplamı (checksum), daha sonra hesaplanacak ve IP başlığına eklenecek. Bu örnekte 0 olarak bırakılmıştır. 1 = checksum hesaplanacak, 0 = checksum hesaplanmayacak
	src_ip_bytes = socket.inet_aton(src_ip)  # Kaynak IP adresini baytlara dönüştürür.
	dst_ip_bytes = socket.inet_aton(dst_ip)  # Hedef IP adresini baytlara dönüştürür.

	ip_header = struct.pack('!BBHHHBBH4s4s', version_ihl, tos, total_length, identification,
							flags_fragment_offset, ttl, protocol, header_checksum, src_ip_bytes, dst_ip_bytes) # IP başlığını paketler ve döndürür. Bu satırda, IP başlığı için gerekli tüm alanlar birleştirilir ve ağ bayt sırasına göre (big-endian) paketlenir.
	return ip_header

# tcp başlığı oluşturmak
def create_tcp_header(src_port, dst_port, seq_num, ack_num, payload_len):
	data_offset = 5  # TCP başlığı uzunluğu (5 * 4 = 20 bayt)
	reserved = 0
	flags = 2  # SYN bayrağı
	window_size = 5840  # Örnek pencere boyutu; bu değer, alıcı tarafın ne kadar veri alabileceğini belirtir. TCP akış kontrolü için kullanılır.
	tcp_checksum = 0  # TCP başlık kontrol toplamı (checksum), daha sonra hesaplanacak ve TCP başlığına eklenecek. Bu örnekte 0 olarak bırakılmıştır.
	tcp_header = struct.pack('!HHLLBBHHH', src_port, dst_port, seq_num, ack_num, (data_offset << 4) + reserved, flags, window_size, tcp_checksum, 0)
	return tcp_header

def send_frame(dst_mac, src_mac, src_ip, dst_ip, src_port, dst_port, payload):
	eth_type = 0x0800  # IP protokolü için Ethernet tipi
	payload_len = len(payload)  # Yük uzunluğunu hesaplar
	
	eth_header = create_eth_header(dst_mac, src_mac, eth_type)  # Ethernet başlığını oluşturur
	ip_header = create_ip_header(src_ip, dst_ip, payload_len)  # IP başlığını oluşturur
	tcp_header = create_tcp_header(src_port, dst_port, seq_num, ack_num, payload_len)  # TCP başlığını oluşturur

	package = eth_header + ip_header + tcp_header + payload  # Ethernet başlığı, IP başlığı, TCP başlığı ve yükü birleştirir
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)  # Ham soket oluşturur
	conn.bind(('eth0', 0))  # 'eth0' yerine uygun ağ arayüzünü kullanın
	conn.send(package)  # Çerçeveyi gönderir
	conn.close()  # Soketi kapatır

	print(f"Frame sent: {len(package)} bytes")  # Gönderilen çerçevenin boyutunu yazdırır

src_mac = b'ff:ff:ff:ff:ff:ff'  # Source MAC address
dst_mac = b'ff:ff:ff:ff:ff:ff'  # Destination MAC address

src_ip = '192.168.32.129'  # Kaynak IP adresi
dst_ip = '192.168.32.130'  # Hedef IP adresi

src_port = 12345  # Kaynak port numarası
dst_port = 12345  # Hedef port numarası

seq_num = 1000  # TCP sıralama numarası; seq_num, TCP bağlantısında gönderilen verilerin sırasını takip etmek için kullanılır. Bu örnekte sabit bir değer kullanılmıştır.
ack_num = 0  # TCP onay numarası

flags = 0x02  # TCP bayrakları (SYN bayrağı), 0x02 = SYN, 0x10 = ACK, 0x18 = PSH + ACK, 0x01 = FIN, 0x04 = RST, 0x08 = URG

payload = b'Hello, World!'  # Gönderilecek veri

send_frame(dst_mac, src_mac, src_ip, dst_ip, src_port, dst_port, payload)  # Çerçeveyi gönderir

