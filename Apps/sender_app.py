import socket
import struct

# Ethernet başlığı oluşturmak
def create_eth_header(dst_mac, src_mac, eth_type):
    return struct.pack("!6s6sH", dst_mac, src_mac, eth_type)

# IP başlığı oluşturmak
def create_ip_header(src_ip, dst_ip, payload_len):
    version_ihl = (4 << 4) + 5  # IPv4 ve IHL
    tos = 0  
    # Toplam uzunluk = IP Başlığı (20) + TCP Başlığı (20) + Veri Uzunluğu
    total_length = 20 + 20 + payload_len  
    identification = 54321  
    flags_fragment_offset = 0  
    ttl = 64  
    protocol = 6  # TCP
    header_checksum = 0  # Ham soketlerde checksum hesaplanmazsa işletim sistemi doldurabilir (OS'e bağlı)
    src_ip_bytes = socket.inet_aton(src_ip)  
    dst_ip_bytes = socket.inet_aton(dst_ip)  

    ip_header = struct.pack('!BBHHHBBH4s4s', version_ihl, tos, total_length, identification,
                            flags_fragment_offset, ttl, protocol, header_checksum, src_ip_bytes, dst_ip_bytes)
    return ip_header

# TCP başlığı oluşturmak
def create_tcp_header(src_port, dst_port, seq_num, ack_num):
    data_offset = 5  # TCP başlığı uzunluğu (5 * 4 = 20 bayt)
    reserved = 0
    flags = 2  # SYN bayrağı
    window_size = 5840  
    tcp_checksum = 0  
    urgent_pointer = 0
    tcp_header = struct.pack('!HHLLBBHHHH', src_port, dst_port, seq_num, ack_num, (data_offset << 4) + reserved, flags, window_size, tcp_checksum, urgent_pointer)
    return tcp_header

def create_http_request(method, path, headers, body):
    request_line = f"{method} {path} HTTP/1.1\r\n" 
    headers_lines = ''.join(f"{key}: {value}\r\n" for key, value in headers.items()) 
    return (request_line + headers_lines + "\r\n" + body).encode() 

# DÜZELTME: seq_num ve ack_num parametre olarak eklendi
def send_frame(dst_mac, src_mac, src_ip, dst_ip, src_port, dst_port, seq_num, ack_num, body):
    eth_type = 0x0800  # IP protokolü için Ethernet tipi
    
    # HTTP isteğini burada oluşturuyoruz ki gerçek boyutunu (payload_len) ölçebilelim
    http_payload = create_http_request("POST", "/", {"Content-Length": str(len(body))}, body)
    payload_len = len(http_payload)  # TCP ve IP'ye bildirilecek net yük boyutu
    
    eth_header = create_eth_header(dst_mac, src_mac, eth_type)  
    ip_header = create_ip_header(src_ip, dst_ip, payload_len)  
    tcp_header = create_tcp_header(src_port, dst_port, seq_num, ack_num)  

    # DÜZELTME: Paket içeriğine http_payload eklendi
    package = eth_header + ip_header + tcp_header + http_payload  
    
    try:
        conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)  
        conn.bind(('eth0', 0))  # Kendi ağ arayüzünle değiştirmeyi unutma (örn: wlan0, en0)
        conn.send(package)  
        print("Paket başarıyla gönderildi!")
    except PermissionError:
        print("Hata: Ham soket (Raw Socket) kullanabilmek için root/administrator yetkisi gerekir (sudo kullanın).")
    finally:
        if 'conn' in locals():
            conn.close()  

# Değişken Tanımlamaları
src_mac = b'\x00\x0a\x95\x9d\x68\x16'  
dst_mac = b'\xff\xff\xff\xff\xff\xff'  

src_ip = '192.168.32.129'  
dst_ip = '192.168.32.130'  

src_port = 12345  
dst_port = 12345  

seq_num = 1000  
ack_num = 0  
body = 'Hello, YouTube!'  

# DÜZELTME: Eksik argümanlar fonksiyon çağrısına eklendi
send_frame(dst_mac, src_mac, src_ip, dst_ip, src_port, dst_port, seq_num, ack_num, body)