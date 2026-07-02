import socket
import struct

def parse_eth_header(data):
    # Ethernet başlığı ilk 14 bayttır: 6 bayt Hedef MAC, 6 bayt Kaynak MAC, 2 bayt Tip
    eth_header = data[:14]
    dst_mac, src_mac, eth_type = struct.unpack("!6s6sH", eth_header)
    
    # MAC adreslerini okunabilir formata çeviriyoruz (örn: 00:0a:95:9d:68:16)
    def format_mac(mac_bytes):
        return ':'.join(f'{b:02x}' for b in mac_bytes)
        
    return format_mac(dst_mac), format_mac(src_mac), eth_type, data[14:]

def parse_ip_header(data):
    # IP başlığının ilk baytı Sürüm ve Başlık Uzunluğunu (IHL) içerir
    version_ihl = data[0]
    ihl = (version_ihl & 0xF) * 4  # IHL kelime (4 bayt) cinsindendir, bayta çeviriyoruz
    
    # İlk 20 baytı paket açıyoruz (IHL değişebilir ama standart minimum 20 bayttır)
    ip_header = struct.unpack("!BBHHHBBH4s4s", data[:20])
    protocol = ip_header[6]
    src_ip = socket.inet_ntoa(ip_header[8])
    dst_ip = socket.inet_ntoa(ip_header[9])
    
    return src_ip, dst_ip, protocol, ihl, data[ihl:]

def parse_tcp_header(data):
    # TCP başlığı minimum 20 bayttır
    tcp_header = struct.unpack("!HHLLBBHHH", data[:20])
    src_port = tcp_header[0]
    dst_port = tcp_header[1]
    seq_num = tcp_header[2]
    ack_num = tcp_header[3]
    
    # Data Offset (TCP başlık uzunluğu) bilgisini alıyoruz
    data_offset = (tcp_header[4] >> 4) * 4
    flags = tcp_header[5]
    
    return src_port, dst_port, seq_num, ack_num, flags, data_offset, data[data_offset:]

def start_listener():
    # 0x0003 -> ETH_P_ALL: Ağ kartına gelen TÜM paketleri (IP, ARP vb.) yakalar
    # NOT: Windows'ta AF_PACKET desteklenmez, bu kod Linux tabanlı sistemler içindir.
    try:
        sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
        sniffer.bind(('eth0', 0))  # Kendi ağ arayüzünle (örn: wlan0) değiştirebilirsin
        print("[-] Dinleyici başlatıldı... Paketler bekleniyor...\n" + "-"*50)
    except PermissionError:
        print("Hata: Dinleyiciyi çalıştırmak için root/sudo yetkisi gereklidir!")
        return

    while True:
        # Paketi al
        raw_data, addr = sniffer.recvfrom(65565)
        
        # 1. ETHERNET KATMANI
        dst_mac, src_mac, eth_type, ip_data = parse_eth_header(raw_data)
        
        # Sadece IP paketlerini (0x0800) inceleyelim
        if eth_type == 0x0800:
            # 2. IP KATMANI
            src_ip, dst_ip, protocol, ip_header_len, tcp_data = parse_ip_header(ip_data)
            
            # Sadece TCP protokolünü (6) filtreleyelim
            if protocol == 6:
                # 3. TCP KATMANI
                src_port, dst_port, seq_num, ack_num, flags, tcp_header_len, payload = parse_tcp_header(tcp_data)
                
                # Bizim gönderdiğimiz 12345 portunu filtreleyelim (Ekranda kirlilik olmasın)
                if src_port == 12345 or dst_port == 12345:
                    print("\n[+] YENİ PAKET YAKALANDI!")
                    print(f"    [Ethernet] Kaynak MAC: {src_mac} -> Hedef MAC: {dst_mac}")
                    print(f"    [IP]       Kaynak IP:  {src_ip} -> Hedef IP:  {dst_ip}")
                    print(f"    [TCP]      Kaynak Port: {src_port} -> Hedef Port: {dst_port}")
                    print(f"    [TCP]      Seq: {seq_num} | Ack: {ack_num} | Flags: {hex(flags)}")
                    
                    # 4. HTTP / PAYLOAD KATMANI
                    if payload:
                        print("    [Payload/HTTP Verisi]:")
                        try:
                            # Gelen veriyi metne dönüştürmeyi dene
                            print(f"\n{payload.decode('utf-8', errors='ignore')}")
                        except Exception:
                            print(f"      [Ham Veri]: {payload}")
                    else:
                        print("    [Payload]: Boş Paket (Sadece TCP Kontrolü)")
                    print("-" * 50)

if __name__ == "__main__":
    start_listener()
