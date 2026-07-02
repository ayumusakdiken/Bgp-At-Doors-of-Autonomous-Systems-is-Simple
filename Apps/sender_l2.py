import socket # ağ iletişimi için soketler oluşturmak ve yönetmek için kullanılır.
import binascii # veri dönüştürme ve bayt dizilerini okunabilir biçime çevirmek için kullanılır.

src_mac = b'\x00\x0c\x29\x4f\x8e\x35'  # Source MAC address
dst_mac = b'\xff\xff\xff\xff\xff\xff'  # Destination MAC address
ether_type = b'0800'  # Ethernet type for IPv4
#
# 0800 : IPv4
# 86DD : IPv6
# 0806 : ARP

# Basit TCP/IP paketleri oluşturmak için bir Python betiği. Bu betik, belirli bir kaynak ve hedef MAC adresi ile bir TCP paketi oluşturur ve bunu bir soket üzerinden gönderir.
payload = b'Hello, this is a TCP packet!'  # Gönderilecek mesaj # b' ' ifadesi, mesajın bayt dizisi (bytes) olarak temsil edildiğini belirtir. Bu, ağ üzerinden gönderilecek verilerin doğru formatta olmasını sağlar.

eth_frame = dst_mac + src_mac + ether_type + payload  # Ethernet çerçevesi başlığı (IPv4). Sıralama : Hedef MAC, Kaynak MAC, Ethernet Tipi, Yük (Payload). Bu, Ethernet çerçevesinin temel yapısını oluşturur.

socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW) # socket.AF_PACKET = Ethernet çerçevelerini doğrudan işlemek için kullanılır, socket.SOCK_RAW = ham soket oluşturmak için kullanılır
socket.bind(('eth0', 0))  # 'eth0' yerine uygun ağ arayüzünü kullanın, eth0 genellikle Linux sistemlerinde varsayılan ağ arayüzüdür.

socket.send(eth_frame)  # Ethernet çerçevesi ve mesajı birleştirip gönderir

socket.close()  # Soketi kapatır

print("TCP packet sent successfully!")  # Gönderim işleminin başarılı olduğunu belirtir
print(f"Sent frame: frame={binascii.hexlify(eth_frame)}, dst_mac={binascii.hexlify(dst_mac)}, src_mac={binascii.hexlify(src_mac)}, eth_type={ether_type}, payload={payload}")  # Gönderilen çerçevenin detaylarını yazdırır. binascii.hexlify() fonksiyonu, bayt dizilerini okunabilir bir hexadecimal formatına dönüştürür.

# İlk 6 byte: Hedef MAC adresi (Destination MAC Address)
# Sonraki 6 byte: Kaynak MAC adresi (Source MAC Address)
# Sonraki 2 byte: Ethernet tipi (Ethernet Type)
# Sonraki byte'lar: Yük (Payload)