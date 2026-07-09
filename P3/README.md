## Konu Başlıkları
- [Statik komşuluk ilişkili BGP EVPN ile VXLAN topoloji egzersizi örneği](#statik-komşuluk-ilişkili-bgp-evpn-ile-vxlan-topoloji-egzersizi-örneği)
  - [`lo` nedir? Neden `lo` sanal arayüzünü kullanıyoruz? `lo` yerine yeni bir sanal ağ arayüzü oluşturup Overlay'i (BGP komşuluk ilişkilerini) neden bunun üzerine kurmadık? Neden `/32` notasyonu kullanıldı?](#lo-nedir-neden-lo-sanal-arayüzünü-kullanıyoruz-lo-yerine-yeni-bir-sanal-ağ-arayüzü-oluşturup-overlayi-bgp-komşuluk-ilişkilerini-neden-bunun-üzerine-kurmadık-neden-32-notasyonu-kullanıldı)
  - [OSPF, `/32` notasyonlu diğer IP adreslerini nasıl buluyor? `/32` notasyonunun mantıksal olarak madem network adresi, subnet'i ve broadcast adresi yok yalnızca tek bir IP olarak var, o halde diğer adresleri nasıl buluyor?](#ospf-32-notasyonlu-diğer-ip-adreslerini-nasıl-buluyor-32-notasyonunun-mantıksal-olarak-madem-network-adresi-subneti-ve-broadcast-adresi-yok-yalnızca-tek-bir-ip-olarak-var-o-halde-diğer-adresleri-nasıl-buluyor)
  - [OSPF'in asıl amacı](#ospfin-asıl-amacı)
  - [Underlay Overlay ayrımının neden yapıldığı üzerine](#underlay-overlay-ayrımının-neden-yapıldığı-üzerine)
  - [RR rolü (`route-reflector-client`) RR olarak belirlenen cihaza gerçekten tanımlandıktan sonra diğer cihazların bundan haberi olacak mı ve nasıl?](#rr-rolü-route-reflector-client-rr-olarak-belirlenen-cihaza-gerçekten-tanımlandıktan-sonra-diğer-cihazların-bundan-haberi-olacak-mı-ve-nasıl)
  - [Address family nedir? Tipleri nelerdir? l2vpn ve l3vpn nedir ve farkı nedir? Address family'i belirtirken ekstra olarak l2vpn'i neden belirttik? sadece l2vpn seklinde yazılsaydi olmuyor muydu?](#address-family-nedir-tipleri-nelerdir-l2vpn-ve-l3vpn-nedir-ve-farkı-nedir-address-familyi-belirtirken-ekstra-olarak-l2vpni-neden-belirttik-sadece-l2vpn-seklinde-yazılsaydi-olmuyor-muydu)
  - [Daha önceden VTEP'in RR'ın client'i olduğunu RR'de `route-reflector-client` şeklinde belirtmemize rağmen neden bir kere daha address-family iç ayarlarında bunu belirtiyoruz?](#daha-önceden-vtepin-rrın-clienti-olduğunu-rrde-route-reflector-client-şeklinde-belirtmemize-rağmen-neden-bir-kere-daha-address-family-iç-ayarlarında-bunu-belirtiyoruz)
  - [Spesifik olarak _"belirli bir VNI değerini duyur"_ diyemez miyiz? Örneğin ağ yapım da iki VNI'im var `10` ve `20` olarak _"sadece 10'u duyur"_ diyemiyor muyum?](#spesifik-olarak-belirli-bir-vni-değerini-duyur-diyemez-miyiz-örneğin-ağ-yapım-da-iki-vniim-var-10-ve-20-olarak-sadece-10u-duyur-diyemiyor-muyum)
  - [FRR'da yapılan tüm konfigürasyon ayarlarını görmek ve `!` işaretinin anlamı](#frrda-yapılan-tüm-konfigürasyon-ayarlarını-görmek-ve--işaretinin-anlamı)
- [iBGP, eBGP ve iBGP ile OSPF arasında ki fark](#ibgp-ebgp-ve-ibgp-ile-ospf-arasında-ki-fark)
- [VPLS + MPLS ve BGP EVPN VXLAN'nin çözdüğü sorun](#vpls--mpls-ve-bgp-evpn-vxlannin-çözdüğü-sorun)
- [Part 2'de yapılan multicast ile flood yöntemi VPLS'mi demek?](#part-2de-yapılan-multicast-ile-flood-yöntemi-vplsmi-demek)
- [Kontrol Düzlemi (Control Plane) ve Veri Düzlemi (Data Plane)](#kontrol-düzlemi-control-plane-ve-veri-düzlemi-data-plane)
- [Protokol nedir? Bir protokol nasıl tasarlanır? Ne ile tasarlanır?](#protokol-nedir-bir-protokol-nasıl-tasarlanır-ne-ile-tasarlanır)
  - [Makine bir paket geldiğinde _"BGP protokolü uygulanacaktır"_ işlemini nereden biliyor/anlıyor?](#makine-bir-paket-geldiğinde-bgp-protokolü-uygulanacaktır-işlemini-nereden-biliyoranlıyor)
  - [Özetle bir protokolün işlenmesi için bir program, arkaplan programı, servis (daemon) tasarlanması mı gerekli? Örneğin C ile bir protokol tasarlanabilir mi? Paketin işlenmesi cihazın paketi servise yönlendirmesiyle oluyorsa paketlenmesi de aynı yerden mi oluyor?](#özetle-bir-protokolün-işlenmesi-için-bir-program-arkaplan-programı-servis-daemon-tasarlanması-mı-gerekli-örneğin-c-ile-bir-protokol-tasarlanabilir-mi-paketin-işlenmesi-cihazın-paketi-servise-yönlendirmesiyle-oluyorsa-paketlenmesi-de-aynı-yerden-mi-oluyor)
  - [Soket programlama kütüphaneleri ağ kartını nasıl programlayabileceğinin hazır kaynakları mı oluyor? Bir C soket programlama kütüphanesi aslında kernel'in ağ kartına nasıl müdahele etmesi gerektiğinin ifadesi mi oluyor?](#soket-programlama-kütüphaneleri-ağ-kartını-nasıl-programlayabileceğinin-hazır-kaynakları-mı-oluyor-bir-c-soket-programlama-kütüphanesi-aslında-kernelin-ağ-kartına-nasıl-müdahele-etmesi-gerektiğinin-ifadesi-mi-oluyor)
  - [Madem bir protokol cihazin ardında çalışan arkaplan servisi o halde TCP veya UDP için bir makine de _udpd_ veya _tcpd_ diye niye bir servis yok?](#madem-bir-protokol-cihazin-ardında-çalışan-arkaplan-servisi-o-halde-tcp-veya-udp-için-bir-makine-de-udpd-veya-tcpd-diye-niye-bir-servis-yok)
- [BGP ve EVPN ayrı kavramlarsa VXLAN flood sorunu için mi geliştirilmişler yoksa bunlar genel bir teknik ama bu sorunu da çözebilecek mahiyette teknikler mi? Flood sorunu olmadan evvel bu teknik veya kavramlar var mıydı? Yoksa flood sorunu üzerine geliştirilmiş teknikler mi?](#bgp-ve-evpn-ayrı-kavramlarsa-vxlan-flood-sorunu-için-mi-geliştirilmişler-yoksa-bunlar-genel-bir-teknik-ama-bu-sorunu-da-çözebilecek-mahiyette-teknikler-mi-flood-sorunu-olmadan-evvel-bu-teknik-veya-kavramlar-var-mıydı-yoksa-flood-sorunu-üzerine-geliştirilmiş-teknikler-mi)
- [RR/Spine/Controller cihazının ağda ki tüm Leaf'e bağlı host'ların MAC adreslerini öğrenme sorumluluğu/rolü flooding yöntemine nazaran tek bir merkeze yüklemek yine performams kaybı oluşturmaz mı?](#rrspinecontroller-cihazının-ağda-ki-tüm-leafe-bağlı-hostların-mac-adreslerini-öğrenme-sorumluluğurolü-flooding-yöntemine-nazaran-tek-bir-merkeze-yüklemek-yine-performams-kaybı-oluşturmaz-mı)
- [PDF'de belirtilen _"dynamic relationship"_ ifadesi ve _"IP atamadan MAC adresini keşfetme"_ vurguları](#pdfde-belirtilen-dynamic-relationship-ifadesi-ve-ip-atamadan-mac-adresini-keşfetme-vurguları)
- [BGP EVPN tablosunda keşfedilmiş MAC adreslerinin bir süre sonra tablodan gitmesi üzerine](#bgp-evpn-tablosunda-keşfedilmiş-mac-adreslerinin-bir-süre-sonra-tablodan-gitmesi-üzerine)
  - [BGP EVPN neden bridge tablosuna bağımlı?](#bgp-evpn-neden-bridge-tablosuna-bağımlı)
  - [Host'un pasif duruma düşmemesi için ağ içinde sürekli ayakta kalabilmesi için çözümler nelerdir?](#hostun-pasif-duruma-düşmemesi-için-ağ-içinde-sürekli-ayakta-kalabilmesi-için-çözümler-nelerdir)
- [ARP proxy ve benzeri teknikler ile ağ cihazları (host'lar vb.) canlı tutulabiliyorsa bu durumda ARP ve MAC tablolarında ki ageing time süresi hiçbir zaman dolmaz. Dolmazsa da kalan iş sadece veriyi göndermek olur (veri trafiği). Böyle bir teknik uygulanabiliyorsa BGP EVPN gibi çözümlere neden ihtiyaç var?](#arp-proxy-ve-benzeri-teknikler-ile-ağ-cihazları-hostlar-vb-canlı-tutulabiliyorsa-bu-durumda-arp-ve-mac-tablolarında-ki-ageing-time-süresi-hiçbir-zaman-dolmaz-dolmazsa-da-kalan-iş-sadece-veriyi-göndermek-olur-veri-trafiği-böyle-bir-teknik-uygulanabiliyorsa-bgp-evpn-gibi-çözümlere-neden-ihtiyaç-var)
- [Bir host'un MAC adresinin BGP EVPN tablosuna kaydedilebilmesinin bir yolu da `ping` atmakdır. Kısaca bu yolla ağda aktif olduğunu göstermek. Ancak bu ARP trafiği oluşturmak demek oluyor. Biz BGP EVPN'i zaten tam da bu amaçla ARP flooding'ten kurtulmak icin kullanmıyor muyduk? Yani ARP atmadan arkaplan da (kontrol düzleminde) cihazlarin birbirlerine paket göndererek (BGP paketleri) kimin ağ da kimin ağ da olmadığını sürekli kontrol eden bir mekanizma ile MAC adresleri elde edilmiyor muydu? O halde neden yine host'dan ping atilarak ARP trafiği oluşturuluyor?](#bir-hostun-mac-adresinin-bgp-evpn-tablosuna-kaydedilebilmesinin-bir-yolu-da-ping-atmakdır-kısaca-bu-yolla-ağda-aktif-olduğunu-göstermek-ancak-bu-arp-trafiği-oluşturmak-demek-oluyor-biz-bgp-evpni-zaten-tam-da-bu-amaçla-arp-floodingten-kurtulmak-icin-kullanmıyor-muyduk-yani-arp-atmadan-arkaplan-da-kontrol-düzleminde-cihazlarin-birbirlerine-paket-göndererek-bgp-paketleri-kimin-ağ-da-kimin-ağ-da-olmadığını-sürekli-kontrol-eden-bir-mekanizma-ile-mac-adresleri-elde-edilmiyor-muydu-o-halde-neden-yine-hostdan-ping-atilarak-arp-trafiği-oluşturuluyor)
- [Eğer ki MAC adresleri, host cihaz pasif duruma geçtiğinde BGP EVPN tablosundan siliniyorsa bu host'un MAC adresi tekrardan nasıl öğreniliyor? Çünkü VTEP'lere host'ların MAC adresleri RR cihazi aracılığıyla yansıtılıyor ama RR cihazı da bu host'un MAC adresini bilmiyorsa ne oluyor? Yani tüm ağ tarafından artık bu host'un MAC adresi bilinmiyorsa ne oluyor tekrardan bilebilmek için?](#eğer-ki-mac-adresleri-host-cihaz-pasif-duruma-geçtiğinde-bgp-evpn-tablosundan-siliniyorsa-bu-hostun-mac-adresi-tekrardan-nasıl-öğreniliyor-çünkü-vteplere-hostların-mac-adresleri-rr-cihazi-aracılığıyla-yansıtılıyor-ama-rr-cihazı-da-bu-hostun-mac-adresini-bilmiyorsa-ne-oluyor-yani-tüm-ağ-tarafından-artık-bu-hostun-mac-adresi-bilinmiyorsa-ne-oluyor-tekrardan-bilebilmek-için)
- [OSPF, BGP vb. tüm bu yapılandırmalar için gerçek senaryolarda gerçekten tek tek her cihaza manuel konfigürasyonlar mı yapılıyor?](#ospf-bgp-vb-tüm-bu-yapılandırmalar-için-gerçek-senaryolarda-gerçekten-tek-tek-her-cihaza-manuel-konfigürasyonlar-mı-yapılıyor)
- [BGP EVPN VXLAN ile host üzerinden yola çıkan bir paketin yolculuğu ve bu yolculukta maruz kaldığı tüm durumlar ve işleyişler](#bgp-evpn-vxlan-ile-host-üzerinden-yola-çıkan-bir-paketin-yolculuğu-ve-bu-yolculukta-maruz-kaldığı-tüm-durumlar-ve-işleyişler)
  - [Bir paketin ilk kez gönderileceği zaman ki yolculuğu](#bir-paketin-ilk-kez-gönderileceği-zaman-ki-yolculuğu)
  - [Bir paketin ikinci kez gönderileceği zaman ki yolculuğu](#bir-paketin-ikinci-kez-gönderileceği-zaman-ki-yolculuğu)
  - [Host'lara IP atanmadan ağ da ilk kez aktif duruma geldiğinde host'larda IPv6 link-local paketleri oluşturulup VTEP'lerin bunu yakalamasının ve RR aracılığıyla diğer VTEP'lere dağıtmasının yolculuğu](#hostlara-ip-atanmadan-ağ-da-ilk-kez-aktif-duruma-geldiğinde-hostlarda-ipv6-link-local-paketleri-oluşturulup-vteplerin-bunu-yakalamasının-ve-rr-aracılığıyla-diğer-vteplere-dağıtmasının-yolculuğu)


## Part 3

### Statik komşuluk ilişkili BGP EVPN ile VXLAN topoloji egzersizi örneği

```
RR ── VTEP-1
```

1. **RR'ye 3 adapter, VTEP'e 2 adapter ver.**
2. **IP planını uygula**

```
RR    → eth0: 10.0.0.1/30  (VTEP'e bağlı taraf)
VTEP  → eth0: 10.0.0.2/30  (RR'ye bağlı taraf)
```
3. **Ayrıca her router'a loopback IP ata**
```
RR   loopback → 1.1.1.1/32
VTEP loopback → 1.1.1.2/32
```

#### `lo` nedir? Neden `lo` sanal arayüzünü kullanıyoruz? `lo` yerine yeni bir sanal ağ arayüzü oluşturup Overlay'i (BGP komşuluk ilişkilerini) neden bunun üzerine kurmadık? Neden `/32` notasyonu kullanıldı?
PDF'te topoloji görselinde **"OSPF Lo + BGP"** yazıyor. **Lo = Loopback** arayüzü. Her router'da `lo` arayüzü vardır — fiziksel bir port değil, sanal. Normalde`127.0.0.1` adresi için kullanılıyor. Ama ağ tasarımında loopback'e özel bir IP atanıyor — örneğin `1.1.1.1/32` gibi. Fiziksel arayüzler bağlantı kesilince kapanabiliyor (Underlay - Overlay ilişkisi). Ama loopback hiçbir zaman kapanmıyor - cihaz çalıştığı sürece aktif. Bu yüzden BGP ve OSPF gibi protokoller loopback IP'sini kullanıyor — daha güvenilir. Part 3'te her VTEP'in loopback adresine `1.1.1.x/32` gibi IP'ler atanıyor. OSPF bu loopback adreslerini fiziksel IP rotaları üzerinden tüm ağa duyuruyor. BGP ise bu loopback adreslerini kullanarak komşuluk kuruyor. Bilgisayarın ethernet kablosunu çekersen o port artık **DOWN** durumuna geçer — yani devre dışı kalır. Linux'ta bunu `ip link set eth0 down` komutuyla da yapabilirsin. `eth0` down olunca o arayüze atanmış IP'ye artık ulaşılamıyor. Yani BGP komşuluğunu `eth0`'ın IP'si üzerinden (fiziksel IP'ler uzerinden) kurmuşsan, kablo çekilince BGP bağlantısı da düşüyor. Ancak cihazlara varsayımsal olarak değişmeyen sabit/unique bir kimlik IP atanırsa ve BGP komşuluk ilişkileri loopback IP'leri uzerinden döndürülüyorsa mevcut router'in port'unda veya arayüzüne erişimde fiziksel bir sorun olursa OSPF bu mevcut cihazın farklı bir arayüzünden (örneğin `eth1`. Eğer ki bu arayüz farklı bir router'ın arayüzüne bağlıysa) bu loopback IP'ye erişimin alternatif bir rotasını bulacaktır. Bu da BGP komşuluk ilişkilerinin üzerinde bir sorun olusturmadan işleyişini sürdürmesini sağlayacaktır. Bu açıklamaya örnek bir senaryo olarak; Router-1 ile Router-2 arasındaki kablo koptu. `eth0` **DOWN** oldu. Ama Router-1'in Router-3'e bağlı `eth1`'i hâlâ çalışıyor. OSPF alternatif yolu buluyor — artık `1.1.1.2`'ye `eth1` üzerinden ulaşılabiliyor. Ama Eğer BGP `10.0.0.1` üzerinden kurulmuşsa (fiziksel IP'ler) — o IP artık yok, BGP düşer. Ama BGP `1.1.1.1` üzerinden kurulmuşsa — loopback hâlâ ayakta, BGP devam eder. Veya IP adresi değişirse; Ağ yeniden yapılandırılıyor, fiziksel IP'ler değişiyor. `10.0.0.1` yerine `172.16.0.1` oldu. BGP fiziksel IP üzerinden kurulmuşsa yeniden yapılandırman gerekir. Ama loopback `1.1.1.1` hiç değişmedi — BGP etkilenmez. Kısaca loopback IP'ye erişimin bir yolu bulunabildiği müddetçe (OSPF'in amaci) BGP komşuluk ilişkileri sürdürülebilir. Zaten tam da bu yüzden komşuluk ilişkileri için `lo` arayüzü kullanılıyor.

Loopback arayüzü yerine teknik olarak yeni bir sanal arayüz de oluşturabilir ve BGP'yi bunun üzerine de kurabilirsin ama `lo` zaten her Linux sisteminde hazır geliyor ve ağ tasarımında **stabil IP** için loopback kullanmak yaygın bir standart haline gelmiş. Herkes anlar, herkes bilir. `/32` notasyonunun kullanılmasının sebebi sabit değişmeyen kimlik IP elde etmek. Bu `/32` notasyonu ile sağlanabiliyor çünkü subnet yok, broadcast yok, sadece IP adresi var. Loopback için ideal — çünkü loopback tek bir cihazı temsil ediyor, subnet gerekmez. Ayrıca loopback arayüzü fiziksel bir port değil — başka bir cihaza bağlı değil. Dolayısıyla subnet gerekmez, sadece tek bir IP yeterli. /32 _"bu sadece bu cihazın kimliği"_ demek. Bu Loopback konusu OSPF ve BGP ile ilişkili olduğundan bu konunun bu aşamaların konfigürasyonlarının yapılması ile daha anlaşılabilir. Özellikle OSPF her cihazın loopback IP'sini tüm ağa duyurduğundan diğer cihazlar _"`1.1.1.2` nerede?"_ diye sorduğunda OSPF _"`10.0.0.2` üzerinden ulaşabilirsin"_ diyecek. Yani loopback'e direkt ulaşılamıyor ama OSPF routing tablosu (rota tablosu) sayesinde ulaşılabiliyor.

#### OSPF, `/32` notasyonlu diğer IP adreslerini nasıl buluyor? `/32` notasyonunun mantıksal olarak madem network adresi, subnet'i ve broadcast adresi yok yalnızca tek bir IP olarak var, o halde diğer adresleri nasıl buluyor?
Route ayarlarını manuel olarak değil de OSPF ile yapıp otomatize ettiğimizde şu sekilde bir konfigürasyon ayarları yaptığımızı hatırlarsak `network 192.168.1.0/24` gibi OSPF mevcut ağ da diğer subnet'lere ulaşımın rotalarını bulup oluşturuyordu. Konfigğrasyonumuza yani `network..` komutunun devamına subnet'in network adresini yazıyorduk. Madem network adresi yazıyoruz o zaman ` network 1.1.1.1/32 ...` tarzında bir OSPF'e tanıtmada bulunduğumuzda OSPF nasıl oluyorda diğer `/32` notasyonlu adresleri bulabilir? tarzInda bir soru yöneltilebilir. Burada OSPF'in davranışlarını bilmek önem arz eder. OSPF'e network komutuyla bir adres yazıldığında OSPF bu adresi iki amaç için kullanıyor:

1. **Hello paketi göndermek için:** _"Bu subnet'te komşu var mı?"_ diye arıyor. `/24` subnet'te bunu yapabilir çünkü birden fazla cihaz var. Ama `/32`'de sadece tek bir IP var — kendisi. Yani `/32` subnet'te komşu araması anlamsız, zaten loopback fiziksel bir port değil.
2. **Duyuru yapmak için:** _"Ben bu adrese sahibim, diğerleri bunu öğrensin."_ İşte `/32` için sadece bu kullanılıyor — komşu aramıyor, sadece _"bu adres bende var"_ diye duyuruyor ve _"şu şekilde bu adrese ulaşabilirsin"_ diyor.

```
network 10.0.0.0/30 area 0 → hem komşu ara hem duyur
network 1.1.1.1/32 area 0  → sadece duyur, komşu arama
```

OSPF `1.1.1.1/32`'yi öğrenince routing tablosuna şunu yazıyor:

```
1.1.1.1/32 via 10.0.0.1, eth0
```

Yani fiziksel bağlantı üzerinden ulaşılabilir hale geliyor — subnet olmasa da. Özetle OSPF'e `network 1.1.1.1/32 area 0` tarzında bir tanıtma yapıldığında `/32` notasyonun mantıksal yönü dolayısıyla zaten network adresi veya diğer adreslere sahip olamayacağını mantıksal olarak anlayıp sadece bu adrese ulaşımın ne üzerinden olacağını duyuruyor. Herhangi bir komsu arama işlemi yapmiyor. OSPF `/32` gördüğünde şunu anlıyor: _"Bu tek bir host adresi, subnet yok, komşu aramaya gerek yok — sadece bu adresin var olduğunu duyurayım."_ Teknik olarak şöyle:

```
/24, /30 gibi → birden fazla IP var → komşu olabilir → Hello gönder
/32           → tek IP → kendisi → komşu olamaz → sadece duyur
```

Ve duyuruyu aldığında diğer cihazlar şunu yapıyor:

```
"1.1.1.2/32 duyuruldu"
        ↓
"Ben 1.1.1.2'ye nasıl ulaşabilirim?"
        ↓
"10.0.0.2 üzerinden ulaşabiliyorum zaten"
        ↓
routing tablosuna yaz: "1.1.1.2/32 via 10.0.0.2, eth0"
```

Yani `/32` adresine ulaşmak için OSPF mevcut fiziksel bağlantıları kullanıyor — yeni bir yol aramıyor, sadece _"bu adres şu next-hop arkasında"_ diyor.

#### OSPF'in asıl amacı
Örneğin yeni bir sanal arayüz tanımladık ve buna IP tanımladık (`20.1.1.1/32` gibi) ve bunu OSPF'e tanıttık `network 20.1.1.1/32 area 0` şeklinde. OSPF yine bu sanal arayüze erişebilmek icin ona önceden tanıtılan fiziksel IP uzerinden mi bu sanal IP'ye ulaşmayı arayacak? Evet, OSPF için önemli olan fiziksel mi sanal mı değil — o adresi başka cihazlara duyurmak ve nasıl ulaşılacağını söylemek. Bu yüzden bir kere tanıtma konfigurasyonu yapıldıktan sonra bu sanal IP'ye ulaşabilecegi bir rota varsa bunun aracılığıyla erişebilindiğini tabloya yazacaktır.

#### Underlay Overlay ayrımının neden yapıldığı üzerine
Bir sorun senaryosu üzerinden ilerlenecek olursa; Elimizde büyük bir veri merkezi var. Binlerce sunucu, onlarca VTEP. Part 2'de VXLAN'ı multicast ile kurduk — çalışıyordu ama ölçeklenme sorunu vardı. Her VTEP bilinmeyen bir paketi MAC adresi temini icin tüm diğer VTEP'lere flood ediyordu. Bu BUM trafiği problemi. Çözüm: VTEP'lerin MAC adreslerini flood yerine kontrol düzleminde öğrenmesi. Yani **"bağırmak"** yerine **"önceden temin".** Bunun için ağ tasarımı kurgusu yapılırken ağın daha net anlaşılabilmesi için underlay ve overlay seklinde ayrım yapılması daha açıklık getirecektir;

- **Underlay = fiziksel ağ.** VTEP'lerin birbirini IP olarak gördüğü gerçek ağ. Burada OSPF çalışıyor — VTEP'ler birbirlerinin IP adreslerini OSPF üzerinden öğreniyor.
- **Overlay = sanal ağ.** VXLAN tünelleri üzerinde çalışan Layer 2 ağı. Host'ların _"aynı switch'e bağlıymış gibi"_ davrandığı katman. Burada **BGP EVPN** çalışıyor — VTEP'ler MAC adreslerini BGP üzerinden öğreniyor.

```
Overlay  → BGP EVPN (MAC adresleri)
───────────────────────────────────
Underlay → OSPF (IP adresleri)
```

Kısaca ayrımın sebebi tamamen overlay yüzündendir. Çünkü Overlay (üst sanal katman sayesinde) üzerinden hem BGP kontrol düzleminde ki işlemleri (MAC adres bilgilerini önceden temin etme) hem de farklı lokasyonları aynı yerel lokasyonda buluşturabilme işlemini (VXLAN overlay IP'leri uzerinden dönüyor) gerçekleştirebiliyoruz. Bu yüzden de overlay, underlay üzerinde koşan bir katman oluyor aslınihayetinde.

4. **OSPF Yapılandırması**

Her router'da loopback IP'sini de OSPF'e tanıtacağız;

RR'de:

```
vtysh
configure terminal
router ospf
network 10.0.0.0/30 area 0
network 1.1.1.1/32 area 0
exit
exit
write
```

VTEP'de (Leaf):

```
vtysh
configure terminal
router ospf
network 10.0.0.0/30 area 0
network 1.1.1.2/32 area 0
exit
exit
write
```

Her iki cihazda da bu yapılandırılmalar yapıldıktan sonra loopback IP'lerinin, fiziksel IP'ler sayesinde bulunduğu `vtysh` konsolundayken;

```
show ip route
```

komutu ile teyit edilebilir. OSPF'e ne belirtilirse bununla ilişkili her türlü rotayı ve adresi bulur. Örneğin farklı bir işlem için cihazlara farklı bir subnet tanımlandığını varsayalım (`192.168.1.0/24` gibi). Bu network adresi OSPF'e bildirilmezse bununla ilgili bir rota yolu bulmayacaktır. Listede loopback IP'leri ne şekilde bulunduğu gösteriliyor örneğin RR cihazında bakarsak;

```
O>* 1.1.1.2/32 [110/10] via 10.0.0.2, eth0, weight 1, 00:06:30
```

tarzında VTEP cihazinin loopback IP'si onun fiziksel IP'si aracılığıyla bulunduğu kaydedilmiş. Şayet RR uzerinden VTEP'e ping atılırsa;

```
ping 1.1.1.2
```

şeklinde paketlerin iletildiği teyit edilebilir. OSPF ayarları yapılmadan evvel bu IP'lere ping atmaya çalışıldığında atılamadı -- hatta doğrudan ve mantıksal olarak `Network Unreachable` çıktısı alındığı görülebilir. Çünkü OSPF `1.1.1.2/32` adresini routing tablosuna şöyle yazdı:

```
O>* 1.1.1.2/32 via 10.0.0.2, eth0
```
Yani routing tablosu diyor ki: _"`1.1.1.2`'ye gitmek istersen `10.0.0.2` üzerinden `eth0`'dan çık."_ RR ping attığında kernel routing tablosuna bakıyor — _"`1.1.1.2` nerede?" — tablo "eth0'dan `10.0.0.2`'ye git"_ diyor. Paket oraya gidiyor. İşte OSPF'in yaptığı şey tam olarak bu — fiziksel bağlantıları keşfedip _"şu IP'ye ulaşmak için şu yolu kullan"_ bilgisini routing tablosuna yazıyor. Sen elle yazmak zorunda kalmıyorsun.

5. **Statik komşuluk ilişkili BGP yapılandırması**

Amacımız BGP komşuluklarını loopback IP'leri üzerinden kuracağımızdan `vtysh`'da bunların BGP konfigürasyonlarında belirtilmesi ve buna göre davrandırılmasi gerek;

RR'da:

```
vtysh
configure terminal
router bgp 1
neighbor 1.1.1.2 remote-as 1
neighbor 1.1.1.2 update-source lo
exit
exit
write
```

Yapılandırmaların açıklamaları;

- `router bgp 1` _"Bu cihazda BGP'yi başlat ve AS numarası 1 olsun"_ demek. Bundan sonra ki komutlar bu BGP instance'ına ait. Kısaca AS 1'de BGP başlatılıyor.
- `neighbor 1.1.1.2 remote-as 1`;
  -  `neighbor 1.1.1.2` → _"komşum `1.1.1.2` IP'sinde"_ — yani VTEP'in loopback adresi
  - `remote-as 1` → _"o komşu da AS 1'de"_ — aynı AS, yani iBGP
- `neighbor 1.1.1.2 update-source lo` - _"Bu komşuya (`1.1.1.2`) BGP mesajları gönderirken kaynak IP olarak `lo` arayüzümü kullan"_ demek. Yani _"ben `1.1.1.1` olarak tanıt kendini"_ diyor. Bunu yazmazsak BGP fiziksel arayüzün IP'sini kullanır — `10.0.0.1` gibi. O fiziksel bağlantı koparsa BGP düşer. Loopback kullanınca fiziksel bağlantı değişse bile BGP ayakta kalır.

VTEP'te BGP yapılandırması:
```
vtysh
configure terminal
router bgp 1
neighbor 1.1.1.1 remote-as 1
neighbor 1.1.1.1 update-source lo
exit
exit
write
```

yapılandırmalar yapıldıktan sonra `vtysh`'da komşuluğun bulunup bulunmadığının teyidi için;

```
show bgp summary
```

her iki cihazın çıktısında da birbirlerinin IP adresleri gözükmesi gerekir.

6. BGP komşuluğu loopback üzerinden kurulduğu teyit edildikten sonra RR olarak belirlediğimiz cihaza gerçekten **RR** rolunu üstletelim. Bunun için RR'de VTEP'i **client** olarak tanımlamamız gerekiyor;

RR'de:
```
vtysh
configure terminal
router bgp 1
neighbor 1.1.1.2 route-reflector-client
exit
exit
write
```

#### RR rolü (`route-reflector-client`) RR olarak belirlenen cihaza gerçekten tanımlandıktan sonra diğer cihazların bundan haberi olacak mı ve nasıl?
VTEP'in (`1.1.1.2`) bundan haberi olacak — BGP mesajlarında RR kendini tanıtıyor. Ama VTEP'te özel bir yapılandırma yapılmasına gerek yok (_"RR cihazin bu dur"_ tarzında). VTEP sadece _"ben bu RR'ın client'ıyım"_ diye davranıyor otomatik olarak.

Özetle;

**RR** → _"sen benim client'ısın, öğrendiğin rotaları bana söyle,
       ben de diğerlerine dağıtırım"_
**VTEP** → _"tamam, öğrendiğim her şeyi sana bildiririm"_

VTEP'in ayrıca _"ben client'ım"_ demesi gerekmiyor — RR tarafında tanımlanması yeterli.

7. **AS 1'in adres ailesini belirleme ve aktif etme (EVPN ayarı)**

RR'de:
```
vtysh
configure terminal
router bgp 1
address-family l2vpn evpn
neighbor 1.1.1.2 activate
neighbor 1.1.1.2 route-reflector-client
exit
exit
exit
write
```

Yapılandırmanın açıklamaları;

- `address-family l2vpn evpn` - BGP'ye _"artık sadece IPv4 rotaları değil, EVPN bilgisi de taşıyacaksın"_ diyoruz. Yani BGP'nin EVPN adres ailesini aktif ediyoruz. **l2vpn = Layer 2 VPN, evpn = Ethernet VPN**. Bunu yazmadan BGP sadece normal IP rotaları taşır — MAC adresleri taşıyamaz. Ayrıca burda bir iç ayara da yani bir iç shell'e daha geçis yapiliyor. 3 kere `exit` yazılmasının sebebi bu.
- `neighbor 1.1.1.2 activate` - _"`1.1.1.2` komşusunu bu adres ailesinde de aktif et"_ demek. Yani _"bu komşuyla EVPN bilgisi de paylaş"_ diyoruz. BGP'de her adres ailesi için ayrıca komşuyu aktif etmen gerekiyor — otomatik gelmiyor.
- `neighbor 1.1.1.2 route-reflector-client` - Bu komut _"`1.1.1.2` benim EVPN adres ailesinde ki client'ım"_ demek. EVPN bilgilerini de yansıt.

VTEP cihazinda da adres ailesi belirlenmeli;

```
vtysh
configure terminal
router bgp 1
address-family l2vpn evpn
neighbor 1.1.1.1 activate
exit
exit
exit
write
```

#### Address family nedir? Tipleri nelerdir? l2vpn ve l3vpn nedir ve farkı nedir? Address family'i belirtirken ekstra olarak l2vpn'i neden belirttik? sadece l2vpn seklinde yazılsaydi olmuyor muydu?
BGP başlangıçta sadece IPv4 rotaları taşımak için tasarlandı. Zamanla farklı türde bilgiler taşıması gerekti (MP-BGP). Bunun için **adres ailesi** kavramı geliştirildi — her adres ailesi farklı türde bilgi taşıyor;
```
ipv4 unicast  → normal IPv4 rotaları (varsayılan)
ipv6 unicast  → IPv6 rotaları
l3vpn         → Layer 3 VPN bilgisi
l2vpn evpn    → Layer 2 MAC adresleri, VXLAN bilgisi
```
EVPN başlangıçta MPLS üzerinde çalışıyordu ve MPLS L2VPN ailesinin bir parçası olarak tanımlandı. Bu yüzden BGP'de `l2vpn evpn` şeklinde yazılıyor — _"L2VPN ailesinin EVPN alt türü"_ demek.

```
address-family
    └── l2vpn
            └── evpn
```

`address-family l2vpn evpn` komutu şunu söylüyor: _"BGP'ye şu andan itibaren MAC adresleri ve VXLAN bilgilerini de taşı."_ Bunu yazmadan BGP sadece normal IP rotaları taşıyor. Bu komutu yazınca BGP'ye yeni bir yetenek ekliyorsun — artık MAC adreslerini de rota gibi işleyebiliyor. Sonrasında yazılan komutlar ise bu yeteneği kiminle ve nasıl kullanacağını belirliyor:

```
address-family l2vpn evpn    → "MAC adresi taşıma moduna gir"
 neighbor 1.1.1.2 activate   → "bu komşuyla MAC adresleri paylaş"
```

Dışarıda kalan normal BGP kısmı ise IP rotalarını taşımaya devam ediyor. Yani iki mod paralel çalışıyor:

```
Normal BGP    → IP rotaları
address-family l2vpn evpn → MAC adresleri + VXLAN bilgisi
```

`l2vpn`'nin alt türleri var bunlardan biri `vpls`'dir. Bu yüzden `address-family l2vpn` komutuna farklı parametreler verilebilir;

```
address-family l2vpn evpn   → EVPN (MAC adresleri, VXLAN)
address-family l2vpn vpls   → VPLS (eski yöntem, MPLS tabanlı)
```

Özetle `l2vpn`, _"Layer 2 bilgisi taşıyacağım"_ diyor, sonrasında ki parametre ise hangi teknikle taşıyacağını belirtiyor. Biz EVPN yazıyoruz çünkü EVPN kullanıyoruz. VPLS yazsaydık eski VPLS yöntemi aktif olurdu. Bu yüzden sadece `address-family l2vpn` yazılamaz — hangi tekniği kullanacağını da belirtmen gerekiyor. Bu yüzden l2vpn sadece _"Layer 2 bilgisi taşıyacağım"_ diyor ama nasıl (hangi yöntem ile) taşıyacağını söylemiyor. EVPN ve VPLS ikisi de Layer 2 bilgisi taşıyor ama çok farklı mekanizmalarla. EVPN MAC adreslerini BGP rotası olarak taşıyor ve kontrol düzleminde öğreniyor. VPLS ise flood ile öğreniyor ve farklı bir format kullanıyor. BGP _"hangi formatta paketleyeyim, hangi kurallara göre işleyeyim?"_ diye soruyor — EVPN ise bunu söylüyor.

`l2vpn` → _"Layer 2 bilgisini taşı"_ diyor ama nasıl formatlanacağını söylemiyor. `evpn` → _"bu Layer 2 bilgisini EVPN formatında formatla"_ diyor. Örnek:

```
l2vpn vpls → MAC bilgisini VPLS formatında paketle
l2vpn evpn → MAC bilgisini EVPN formatında paketle
```

İkisi de MAC adresi taşıyor ama format farklı. EVPN formatında şunlar var:

```
- Route Type (type-2, type-3 gibi)
- Route Distinguisher
- Route Target
- VNI bilgisi
- Encapsulation tipi (VXLAN, MPLS)
```

VPLS formatında bunlar yok — daha basit ve eski bir format. Yani `l2vpn` **ne taşıyacağını** söylüyor, `evpn` ise **nasıl paketleyeceğini** söylüyor. İleri ki aşamalarda `show bgp l2vpn evpn` komutuyla RR'de ki BGP EVPN tablosunda ki `[2]:[0]:[48]:[MAC]` formatı tam olarak EVPN formatı — `l2vpn vpls` yazsaydık bu format farklı olurdu ve VXLAN ile çalışmazdı.

Yani burada teknik ifade ile;

- **AFI (Address Family - Ne taşıyoruz?):** l2vpn komutu BGP'ye _"Biz bu komutun altında Katman 2 (Layer 2) ağ bilgisini taşıyacağız"_ talimatını verir.
- **SAFI (Subsequent Address Family - Nasıl paketliyoruz?):** evpn veya vpls komutu ise _"Bu Katman 2 bilgisini hangi formata, hangi kurallara ve hangi attribute'lara (özniteliklere) göre paketleyip komşuma göndereceğim?"_ sorusunun cevabıdır.

Kısaca RR (Route Reflector) cihazında görülen o format, **RFC 7432** standartlarında tanımlanmış olan EVPN Route Type 2 (MAC/IP Advertisement Route) paketleme formatidir. FRR veya diğer network cihazlarında gördüğün bu ifadenin parçaları tam olarak şunları söyler:

```
[2]: Route Type 2 (Yani bu rota bir MAC/IP duyurusudur).
[0]: Ethernet Tag ID (VLAN bilgisi veya default olarak 0).
[48]: MAC adresinin bit uzunluğu (MAC adresleri 48 bittir).
[MAC]: Hostun gerçek MAC adresi.
```

#### Daha önceden VTEP'in RR'ın client'i olduğunu RR'de `route-reflector-client` şeklinde belirtmemize rağmen neden bir kere daha address-family iç ayarlarında bunu belirtiyoruz?

`route-reflector-client` iki yerde yazılabilir:

- Global BGP seviyesinde:
```
router bgp 1
 neighbor 1.1.1.2 route-reflector-client
```
Bu tüm adres aileleri için geçerli oluyor.

 - Address-family seviyesinde:
```
address-family l2vpn evpn
 neighbor 1.1.1.2 route-reflector-client
```
Bu sadece EVPN adres ailesi için geçerli oluyor. Ayrıca bu komutu address-family içinde yazmadan da Leaf cihazı RR'ı **"RR"** cihazı olarak gördüyse bu şu anlama geliyor: Global seviyede tanımlanmış `route-reflector-client` EVPN adres ailesine de yansımış. Ama iyi pratik olarak her adres ailesinde ayrıca belirtmek daha net ve güvenli — özellikle birden fazla adres ailesi varsa hangi adres ailesinde RR olduğu açıkça belli oluyor.

8. **VXLAN kurulumu**
VXLAN arayüzünü VTEP'te oluşturalım. Ama bu sefer multicast veya statik mod kullanmayacağız — BGP EVPN otomatik halledecek (bu şekilde halletmesi şeklinde ayarlayacğımızdan);

VTEP'de:
```
ip link add vxlan10 type vxlan id 10 local 1.1.1.2 nolearning dstport 4789
ip link set vxlan10 up
```

- `nolearning` parametresi şu anlama geliyor - _"Bu VXLAN arayüzü MAC adreslerini veri düzleminde öğrenmesin."_ Yani normal VXLAN'da bir paket geldiğinde VTEP _"bu MAC adresi şu yerden geldi"_ diye tabloya yazıyordu — **data plane learning.** Bu flooding'e yol açıyordu. `nolearning` ile VTEP diyoruz ki: _"MAC adreslerini kendin öğrenmeyeceksin, BGP EVPN sana söyleyecek."_

- `nolearning` olmadan → veri düzleminde MAC öğren (flood)
- `nolearning` ile → kontrol düzleminde MAC öğren (BGP EVPN)

İşte BGP EVPN'in farkı tam burada. Flooding yerine kontrol düzleminde önceden MAC adresini temin etmek.

9. **Bridge kurulumu**

Yine VTEP'de:
```
ip link add br0 type bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth1 master br0
```

10. **VTEP'te EVPN yapılandırmasını tamamlama;**

```
vtysh
configure terminal
router bgp 1
address-family l2vpn evpn
advertise-all-vni
exit
exit
exit
write
```

- `advertise-all-vni` ayarı şunu söylüyor: _"Bu cihazda tanımlı tüm VXLAN ID'lerini BGP EVPN üzerinden duyur."_ Yani VTEP _"bende VNI 10 var"_ diye RR'ye bildiriyor. RR bunu diğer VTEP'lere yansıtacak.

#### Spesifik olarak _"belirli bir VNI değerini duyur"_ diyemez miyiz? Örneğin ağ yapım da iki VNI'im var `10` ve `20` olarak _"sadece 10'u duyur"_ diyemiyor muyum?

Hayır — ya hepsini duyurursun (`advertise-all-vni`) ya da tek tek tanımlarsın;

```
address-family l2vpn evpn
 advertise-all-vni    ← tüm VNI'leri duyur
```

Yerine spesifik VNI degerini tek tek tanımlamak için;

```
vni 10
 rd 1.1.1.2:10
 route-target import 1:10
 route-target export 1:10
```

Eğer 100 VNI varsa her birini tek tek tanımlamak çok zahmetli. `advertise-all-vni` hepsini otomatik duyuruyor. Ortası yok. Ama eğer VNI 20'yi bridge'e bağlamadıysan veya `ip link add vxlan20` ile oluşturmadıysan `advertise-all-vni` yazmış olsan bile VNI 20 duyurulmaz. Çünkü VTEP sadece gerçekten var olan (işleyişte olan) VNI'leri duyuruyor.

Yani kontrol mekanizman şu:

```
advertise-all-vni → "var olan tüm VNI'leri duyur"
VNI oluşturma     → hangilerinin var olacağını sen belirliyorsun
```

VNI 20'yi oluşturmasan ve `advertise-all-vni` yazmış olsan bile duyurulmaz. Bu şekilde dolaylı olarak kontrol edebiliyorsun.

11. **BGP EVPN tablosu incelemesi**

Son ayardan sonra RR'de sunu calistir;

```
show bgp l2vpn evpn
```

Bu tablo BGP EVPN'in öğrendiği rotaları gösteriyor — kontrol düzleminin tablosu;

- `*>i`:
  - `*` → rota geçerli
  - `>` → en iyi rota seçildi
  - `i` → iBGP'den öğrenildi
- `Route Distinguisher: 1.1.1.2:2` - Bu rotanın sahibi `1.1.1.2` — yani VTEP. Her VTEP'in benzersiz bir RD'si var, rotaların kimin olduğunu belirtiyor.
- `[3]:[0]:[32]:[1.1.1.2]` - Bu bir Type-3 prefix. Bu tablonun listelenmesinde kullanılan **Type** numaraları vardır. Her bir numara belirli bilgileri sıralar. Örneğin Type-3 şunu söylüyor: _"`1.1.1.2` adresinde ki VTEP VNI 10'da mevcut"_ — VTEP kendini duyuruyor.
- `RT:1:10` **Route Target** — _"bu rota VNI 10'a ait"_ demek.
- `ET:8` **Encapsulation Type 8 = VXLAN** -- _"Bu rota VXLAN kapsülleme kullanıyor"_ demek.

Ancak burada asıl önemli olan ve gözükmesi gereken bilgi host'un RR'de ki MAC bilgisidir. Bu nokta da ağa bir host cihazi ekleyelim ve bunu VTEP'in `eth1` arayüzüne bağlayalım. Ardından host'u ayağa kaldıralım. Host'a herhangi bir IP adresi atamadan VTEP'e bağlanan host cihazının VTEP tarafından MAC adresinin saptanıp bunu RR cihazına bildirip bildirmediğine bakmak için; host ayağa kaldırıldıktan sonra RR'de `show bgp l2vpn evpn` ile çıktı al. Type-2 prefix'inde host'un MAC adresi gözüküyorsa bu IP atamadan da host'ların MAC adres bilgilerinin elde edilğini gosterir. VTEP'de de `show bgp l2vpn evpn` diyerek kendi tablosunda da mevcut olup olmadığı teyit edilebilir. RR'de BGP EVPN tablosu incelenirse Type-2 prefix'de ki semboller şu sekilde ifade edilebilir;

```
[2] → Type-2, MAC adresi duyurusu
[0] → Ethernet tag
[48] → MAC adresinin bit uzunluğu (48 bit = 6 byte, standart MAC)
[02:42:da:5d:50:00] → Host'un MAC adresi.
Next Hop: 1.1.1.2 → bu MAC 1.1.1.2 VTEP'inde
RT:1:10 → VNI 10'a ait
```

Yani RR şunu öğrendi: `02:42:da:5d:50:00` (örnek bir MAC adresi bu host'un kendi MAC adresine bakip doğrulanabilir) _"MAC adresi `1.1.1.2` VTEP'inde, **VNI 10'da**."_ Bu bilgiyi başka bir VTEP ağa eklenseydi anında RR tarafından ona yansıtlacaktı — flooding olmadan, direkt. Özetle bu yapı ile MAC adresleri dinamik olarak bir tabloda RR cihazi sayesinde toplanip tabloya kaydedilip diğer cihazlara dağıtılıyor ve cihazlar MAC adreslerini önceden bildikleri için ağı yormadan doğrudan veri düzleminde paket gönderimi yapabiliyorlar. Burada **dinamiklikten** kasıt ağda ki cihazların aktiflik ve pasifliğine bağlılığı. Örneğin bir host ağdan ayrılırsa VTEP bunu BGP üzerinden duyurur ve tablo güncellenir. Yani tablo canlı ve dinamik.

ve BGP EVPN tablosu şöyle çalışıyor:

```
Host bağlandı  → Type-2 duyurusu geldi, tabloya eklendi
Host aktif     → tablo güncelleniyor
Host ayrıldı   → VTEP "bu MAC artık yok" diye BGP withdraw mesajı gönderiyor
               → RR tablodan siliyor, diğer VTEP'lere bildiriyor
```

Yani tablo:

- Aktif değişikliklere anında tepki veriyor
- Gereksiz yere silmiyor
- Ağ değişmedikçe bilgi orada duruyor

```
1. Host ağa bağlandı
        ↓
2. VTEP MAC adresini öğrendi
        ↓
3. VTEP → RR'ye BGP EVPN Type-2 duyurusu
        ↓
4. RR → diğer tüm VTEP'lere yansıttı
        ↓
5. Diğer VTEP'ler "bu MAC 1.1.1.2'de" biliyor
        ↓
6. Paket gönderilecekse direkt VXLAN tüneli açılıyor
   flood yok, gereksiz trafik yok
```

12. **Ağa diğer VTEP'leri ekleme**
Burada da VTEP-1 ile RR'da yapılan konfigürasyonların benzerini yine yeni VTEP'ler için de uygulanması gerek uygun subnet vb. işlemler yapılarak;

Özetle yeniden;

-  **RR ve yeni VTEP arası subnet oluşturmak.**
- **Yeni VTEP'e overlay için `lo` arayüzüne yeni bir kimlik IP atamak `1.1.1.3` gibi**
- **Yeni VTEP'de OSPF yapılandırması;**
```
vtysh
configure terminal
router ospf
network 10.0.0.4/30 area 0
network 1.1.1.3/32 area 0
exit
exit
write
```

- **RR'da da yeni subnet'i OSPF'e tanıtmak;**
```
vtysh
configure terminal
router ospf
network 10.0.0.4/30 area 0
exit
exit
write
```

- **Yeni VTEP'de BGP konfigurasyonu**;
```
vtysh
configure terminal
router bgp 1
neighbor 1.1.1.1 remote-as 1
neighbor 1.1.1.1 update-source lo
!
address-family l2vpn evpn
neighbor 1.1.1.1 activate
advertise-all-vni
exit
exit
exit
write
```

- **RR'de**
```
vtysh
configure terminal
router bgp 1
neighbor 1.1.1.3 remote-as 1
neighbor 1.1.1.3 update-source lo
!
address-family l2vpn evpn
neighbor 1.1.1.3 activate
neighbor 1.1.1.3 route-reflector-client
exit-address-family
exit
exit
write
```


#### FRR'da yapılan tüm konfigürasyon ayarlarını görmek ve `!` işaretinin anlamı
`!` işareti yorum satırı — yani boş satır veya ayırıcı görevi görüyor. FRR'de `!` ile başlayan satırlar yorum olarak işleniyor, çalıştırılmıyor. Cisco router'larında da aynı şekilde kullanılıyor — config dosyalarını bölümlere ayırmak için. Tüm FRR yapılandırmasını görmek için; 

```
show running-config
```

komutu kullanılabilir.

- **yeni VTEP'de VXLAN ve bridge kurulumu;**
```
ip link add vxlan10 type vxlan id 10 dstport 4789 local 1.1.1.3 nolearning
ip link set vxlan10 up
ip link add br0 type bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth1 master br0
```
_Kendi topolojine göre yeni VTEP için host'a bağlı arayüzü kontrol et — `eth1` mi `eth0` mı?_

- **Yeni VTEP'in arkasına yeni bir host bağla ve onu çalıştır ardından tüm VTEP ve RR cihazında bu host'un MAC adresinin BGP EVPN tablosuna geldiğini teyit et**

```
show bgp l2vpn evpn
```

Özet olarak bu biçimde kurgulanmış bir ağın davranışı;
- **Başlangıç durumu:** Yeni bir VTEP ağa ekleniyor.
- **Birinci adım** olarak OSPF devreye giriyor — yeni VTEP loopback adresini OSPF'e tanıtıyor, diğer tüm VTEP'ler bu loopback adresini öğreniyor.
- **İkinci adım** olarak BGP kuruluyor — yeni VTEP sadece RR ile BGP komşuluğu kuruyor. RR onu diğer VTEP'lere tanıtıyor.
- **Üçüncü adım** olarak bir host bağlanıyor — VTEP bu host'un MAC adresini öğreniyor, BGP EVPN üzerinden RR'ye bildiriyor, RR diğer tüm VTEP'lere dağıtıyor.
- **Dördüncü adım** olarak veri akışı başlıyor — başka bir host bu MAC'e paket göndermek istediğinde VTEP RR'ye sormadan biliyor nerede olduğunu, direkt VXLAN tüneli açıp gönderiyor.
### iBGP, eBGP ve iBGP ile OSPF arasında ki fark

BGP (Border Gateway Protocol), AS'ler arasında _"ben şu IP adreslerine ulaşabiliyorum, benden geç"_ diye konuşulan protokol. Basitçe şöyle çalışır:

```
AS1 (Türk Telekom)        AS2 (Google)
┌─────────────┐           ┌─────────────┐
│             │◄─────────►│             │
│  BGP Router │   "Ben    │  BGP Router │
│             │ 8.8.8.0/24│             │
└─────────────┘ bilirim!" └─────────────┘
```

### VPLS + MPLS ve BGP EVPN VXLAN'nin çözdüğü sorun
Veri merkezlerinin yaygınlaşmadığı zamanlarda telekomünikasyon ağlarında **VPLS + MPLS** teknikleri kullanılıyordu. VPLS + MPLS, VXLAN'nın alternatifi olarak düşünülebilir. Farkları MPLS'in ağda uygulanabilmesi için özel donanım gerektirmesidir (**PE: Provider Edge Device** (VPLS + MPLS'li ağlarda ki literatürde VTEP yerine bu kullanılıyor)); çünkü IP paketinin içeriğine hiç dokunmayıp sadece paketin dışına MPLS etiketi konuluyor ve router yalnızca bu etikete bakıp ona göre yönlendirme yapıyor. Bu da tüm ağda ki cihazların MPLS etiketini anlayabileceği donanıma sahip olması ve bu cihazlara MPLS konfigürasyonu uygulanması demek. Yani veri düzlemin de MPLS, paketleri etiketleyen ve taşıyan bir taşıyıcıdır. Ancak tek başına bu teknik farklı lokasyonları aynıymış gibi yapamadığından **VPLS**, MPLS'e (VPLS zaten MPLS üzerinde çalışan bir servis) tıpkı VXLAN'ın yaptığı gibi farklı lokasyonları birbirlerine sanal bir ortam da bağlayarak aynı ortamdaymış havası verme davranışını sağlıyordu ancak bunu flood methoduyla yapıyordu. Yani hedef MAC adresini öğrenebilmek için tüm ağa duyuru yapmak (BUM trafiği). Telekom ağlarda kullanılan bu method veri merkezleri içinde de uyarlanmaya çalışıldı ancak bu yöntem veri merkezlerinin büyümesi ve yaygınlaşmasıyla ağa performanssal kayıp oluşturmaya başladı. Bu yüzden çözüm olarak MAC adreslerinin öğrenilmesinin farklı bir tekniği ve kombinasyonu meydana getirildi. **BGP EVPN + MPLS.** Ağ da paketler MPLS ile yine etiketleniyor ve taşınıyor ancak hedefin MAC adresi artık daha kontrollü şekilde BGP ile öğreniliyor. **BGP EVPN + VXLAN** ise aynısının alternatifidir. Paketler etiketlenmiyor bunun yerine kapsülleniyor ve özel donanım gerektirmiyor (Standart IP cihazları ile çalışabilir). Böylece ağ da özel ve pahalı donanım gerektirmeden IP cihazları ile ucuz biçim de veri merkezi ağ yapısı oluşturulabiliyor. Peki neden halen telekom ağlarda BGP EVPN + MPLS kullanılıyor? Eğer bir servis sağlayıcıysan (Türk Telekom, Vodafone vb.) zaten halihazırda devasa bir MPLS donanımlı ağın vardır. Yeni bir teknoloji olan VXLAN'a geçmek istediğinde tüm altyapıyı (IP Underlay olarak) değiştirmek yerine, sadece uçtaki router'lara _"Artık VPLS gibi flooding yapmayın, EVPN gibi akıllıca BGP konuşun ama veriyi yine bildiğimiz MPLS etiketleriyle taşıyın"_ dersin.

Özetle:
 - **VPLS + MPLS:** Eski nesil, flooding (su baskını) yapan, hantal yapı.
 - **EVPN + MPLS:** Yeni nesil, akıllı (BGP), performanslı yapı (Genelde WAN'da).
 - **EVPN + VXLAN:** Yeni nesil, akıllı, standart IP cihazlarla çalışan yapı (Genelde Data Center'da).

Part 2'de uygulanan dinamik multicast modu ile oluşturulmuş bir VXLAN ağı, statik mod (unicast) ile oluşturulmuş bir VXLAN ağa nazaran daha performanslı çalışır. Ancak multicast VXLAN'ın da bir limiti vardır. VTEP cihazlarının fazlalaşması, (örneğin 100 veya 1000 VTEP) flood methodu ile MAC adresi bilgisi öğrenmeye çalışan bütün VTEP cihazlarını yorar. Çünkü tek bir MAC adresi bilgisini temin etmek için bütün ağda ki cihazlara bağırılma durumu olmaktadır. Bu da doğal olarak az VTEP cihazı bulunduran bir ağa nazaran performans kaybı yaşatır. Ortaya çıkan bu soruna çözüm olarak BGP EVPN tekniği meydana getirilmiştir. Kabaca VTEP cihazları MAC adres bilgisi öğrenmek için multicast grubunda ki bütün cihazlara bunu sormak yerine artık VTEP'e cihazın MAC adresinin hangi VTEP'in arkasında olduğunu söyleyen omurga cihazı ağa konuluyor. Bu cihaza **Spine/RR(Route Reflector)/Controller** deniyor. Tüm VTEP'ler bu omurga cihaza bağlanılıyor ve artık VTEP'ler (veya diğer bir adıyla **Leafs**) MAC adres bilgilerini bu omurga cihazdan alıyorlar. Omurga cihaz öğrendiği her bir MAC adresini ona baglo olan her bir leaf'e gonderiyor. Bu haberleşme işleminin protokolü **BGP EVPN** ile sağlanıyor. Özetle veri merkezlerinde şu sorun var: Farklı fiziksel lokasyonlardaki sunucular aynı Layer 2 ağdaymış gibi davranmalı. Bunu çözmek için geleneksel flood yöntemi hantal. Part 3, Part 2'nin devamı niteliğinde bir temaya sahip. Statik veya dinamik mod şeklinde ayarlanmayacak VXLAN yapılı bir ağ için BGP EVPN tekniği kullanan bir mimari kurgulanması gerekiyor. Ayrıca proje dökümanında MPLS kullanmadan demesinin sebebinin ilki MPLS icin özel donanıma ve yazılıma ihtiyaç olmasıdır. ikincisi ise bu kombinasyonun (BGP EVPN + VXLAN) veri merkezlerinde kullanılması ve yeni nesil olması ve özel donanım gerektirmeden (MPLS gibi) standart IP cihazlarında çalışmasını tanıtmaktır. Veri merkezlerinde ki bu altyapısal yenilik part 3 konsepti içinde tanıtılmayı amaçlıyor.
### Part 2'de yapılan multicast ile flood yöntemi VPLS'mi demek?
Multicast modunda bir VXLAN yapısı kurulduğu zaman VPLS ile VXLAN yapısı oluşturmuş olunmaz. Biz veri düzlemi seviyesinde multicast modu aracılığıyla ve flood methoduyla MAC adreslerini elde etme mekaniğini kullanmış oluyoruz VPLS kullanmış olmuyoruz. VPLS tamamen farklı bir teknikdir. Ancak hem VPLS hem de VXLAN'in temel amacı aynıdır: Farklı yerlerdeki Layer 2 (Lokal) ağları, arada bir Layer 3 ağ olmasına rağmen sanki aynı switch'e bağlıymış gibi birbirine bağlamak. Her iki teknik de statik modlarında bir paketin nereye gideceğini bilmediğinde (BUM trafik: Broadcast, Unknown Unicast, Multicast) paketi her yere kopyalar (Flood). Paket geri dönerken de _"bu MAC adresi şu uçtaymış"_ diyerek öğrenir (Learn);

**VXLAN**, standart bir IP ağı (Underlay) üzerinde çalışır. Paketleri IP/UDP içine sarar.
- **Nasıl Taşır?:** Klasik bir IP yönlendirmesi (OSPF, ISIS, BGP hatta Static Route) olan her yerde VXLAN çalıştırabilirsin.
- **Multicast'in Rolü:** VXLAN'de multicast, sadece ortak alan görevi görür. Ağdaki bir VTEP (VXLAN ucu), bilmediği bir MAC adresini ararken paketi multicast grubuna gönderir. O gruba üye olan diğer VTEP'ler paketi alır. Yani multicast, VXLAN'in içindeki trafiği dağıtmak için kullandığı bir araçtır, teknolojinin kendisi değildir.

**VPLS** ise bir MPLS (Multiprotocol Label Switching) teknolojisidir. Paketleri IP içine değil, MPLS etiketleri (labels) içine sarar.
- **Nasıl Taşır?:** VPLS çalıştırabilmek için ağındaki tüm cihazların MPLS desteklemesi, arkada BGP gibi protokollerle **Pseudowire (sanal kablo)** tünelleri kurması gerekir.
- **Flood Mekanizması:** VPLS'te multicast grubu kullanılmaz. Bunun yerine uç cihazlar (PE - Provider Edge) arasında tam örgü (Full-Mesh) sanal kablolar kurulur. Bir yayın (broadcast) geldiğinde, cihaz bu paketi tüm sanal kablolara tek tek kopyalayarak gönderir (Head-end Replication).
### Kontrol Düzlemi (Control Plane) ve Veri Düzlemi (Data Plane)
Bir ağın işleyişi özetle iki ayrı katmanda/düzlemde ele alınabilir; kontrol ve veri. Bir ağ kendi yapısının kontrolünü yönetilebilir ve yönetilemeyen cihazlar üzerinden sağlar. Aynı şekilde yönetilebilir bir ağ cihazı aynı zaman da veri iletim için de kullanılabilir. Her yönetilebilir ağ cihazı iki düzleme sahiptir; kontrol ve veri düzlemi ve buna müteakip bu düzlemlerde kontrol ve veri trafikleri oluşur.

Bir ağ da **yönetilemeyen** ve **yönetilebilen** olarak iki cihaz çeşidi bulunabilir;

- **Unmanaged Switch'ler:** Sadece veri düzlemine sahiptir denilebilir. İçinde bir işletim sistemi veya karar mekanizması yoktur bu yüzden gelen sinyali basit bir tabloya göre iletir.
- **Yönetilebilir Cihazlar (Router, Switch):** Kesinlikle her iki düzleme de sahiptir. Çünkü bu cihazların bir CPU'su, bir işletim sistemi (IOS, FRR, Junos vb.) ve bir yönetim arayüzü (SSH, Konsol) vardır. Bu yönetimsel süreçlerin tamamı Kontrol Düzlemi'nde döner.

**Kontrol düzlemi/tabanında** işlem yapan cihazlar; _"en kısa rota hesaplaması, MAC adres bilgisini öğrenme, hangi cihazların ağdan düştüğünü veya ağa katıldığını"_ vb. işlemleri hesapladıklarından CPU gücünden yararlanırlar. MAC, komşuluk ilişkileri, route tablosu vb. oluşturup hazırlar ve güncellerler.

**Veri düzlemi/tabanında** işlemler ise sadece **kas gücüdür**. Kontrol düzlemi (CPU) kararı verdikten sonra bir tablo oluşturur ve bu tabloyu **ASIC (Application-Specific Integrated Circuit)** denilen özel çiplere kopyalar. ASIC, sadece tek bir işi (paket yönlendirme) yapmak için üretilmiş süper hızlı bir yongadır. Mantık yürütmez, sadece tabloya bakar: _"Paket A portundan geldi, hedefi B IP'si, o zaman C port"_ gibi. Sadece paketleri iletir. Gelen paketin başlığına bakar, tabloda eşleşen yere gönderir. Hiçbir _"hesaplama"_ veya _"karar verme"_ süreciyle ilgilenmez. ASIC'ler donanım seviyesinde çalıştığı için gecikme (latency) neredeyse sıfırdır. Bu sayede veriyi saniyeler içinde iletebilirler.

OSPF, BGP vb. protokol ve teknikler ile kontrol düzleminde işlem yapan cihazların iletişimi otomatikleştirilip ağ dinamik (otomatizasyon) hale getirilebilir. Bu düzlemere takiben bir ağ da iki tip trafik olur bunlar; **kontrol** ve **veri trafiğidir**;

**Kontrol trafiği**, kontrol düzleminde işlem yapan cihazlar arasında ki teyitlerdir. Bu, ağ üzerinden diğer cihazlara kontrol paketleri iletilerek kontrol edilir örneğin;

- **ARP (Address Resolution Protocol):** Bir cihazın IP adresini bilip MAC adresini bunun üzerinden öğrenmeye çalıştığı ve sorduğu _"Kimde bu IP var?"_ sorusu bir kontrol trafiğidir.
- **Keepalive (Hayatta mısın?) Paketleri:** BGP komşuları (mesela bir Leaf ile RR) birbirine sürekli minik paketler atar. _"Ben buradayım, hala çalışıyorum"_ derler. Eğer bu kontrol paketleri kesilirse, cihazlar o yolun çöktüğünü anlar ve trafiği keser. Aynı şekilde OSPF'de komşuları ile buna benzer biçimde işler. 

**Veri trafiği** ise, veri düzleminde işlem yapan cihazlar arasında ki doğrudan veri iletimleridir. Asıl kullanıcı verisinin (YouTube videosu, dosya transferi, ping paketi) geçtiği yerdir. Donanım (ASIC çipler) üzerinde çalışır. Kontrol düzlemi _"adres ve rote şu dur"_ der, veri düzlemi ise paketi oraya taşır. Bu ayrımın olmasının sebebi örneğin; eğer bir cihazda kontrol düzlemi (CPU) çok meşgul olursa (örneğin çok karmaşık BGP hesaplamaları yapıyorsa), veri düzlemi (ASIC) bundan etkilenmez. Yani cihaz yeni yollar hesaplarken, mevcut paketleri iletmeye tam hızda devam edebilir. Bu da bir cihazda iki farklı iş birbirlerini etkilemeden yapılabilir anlamına gelip bir cihaz farkli rollerde işler yapabilir anlamına gelir.

Özetle bir ağda ki işleyiş iki düzlem de oluyor; biri kontrol diğeri veri. Kontrol düzleminde ki ağ cihazları; MAC ve route tablosu, en kısa rota hesaplama vb. karmaşık hesaplamaların yapıldığı düzlemdir. Aynı zaman da buna ARP, OSPF ve BGP komşuluk iletişimi gibi kontrol trafiği de dahil edilebilir. Veri düzleminde ise kontrol trafiğinin hazırladğı en kısa rota bilgisi, MAC ve route gibi tablolardan yola çıkarak sadece hedefe verinin taşınması düzlemidir. Bu yüzden kontrol düzlemi işlemleri için CPU, veri düzleminde ki işlemler için ASIC donanım kullanılır. Ayrıca bu iki bileşen genelde tek bir cihaz da bulunduğundan bir ağ cihazı aslında iki düzlemde çalışabilir potansiyeldedir ve zaten çalışır. Örnek olarak Wireshark'da görülen ARP isteği _"Who has 192.168.1.1? Tell 192.168.1.2"_ mesajları tam olarak kontrol düzlemi trafiğinin paketleridir. Ping atmadan önce cihaz _"bu IP'nin MAC adresi nedir?"_ diye soruyor — bu bir kontrol sorusu, veri taşımıyor. Cevabı öğrenince MAC tablosuna yazıyor, sonra gerçek veriyi gönderiyor.

```
ARP → "MAC adresin nedir?" → kontrol düzlemi
ICMP ping → gerçek veri → veri düzlemi
```

BGP EVPN'in çözdüğü sorun da tam burada: Normal VXLAN'da VTEP bilinmeyen bir MAC için ARP flood yapıyor — tüm ağa _"bu MAC kimde?"_ diye bağırıyor. BGP EVPN ile ise bu bilgi zaten kontrol düzleminde önceden dağıtılmış — ARP flood'a gerek kalmıyor.

### Protokol nedir? Bir protokol nasıl tasarlanır? Ne ile tasarlanır?

Bir cihazda bir paket oluşturmak veya bir paketin çözümlenmesi işlemleri cihazin bunları yapabilecek mahiyette **programa/uygulamaya** sahip olmasını gerektirir. Bu program aslında paketin nasıl paketlenmesi ve işlenmesi gerektiğinin belirtimleridir. Yani aslında protokoldür. Bu yüzden bir programalama dili ile özel bir protokol tasarlamak mümkündür.

#### Makine bir paket geldiğinde _"BGP protokolü uygulanacaktır"_ işlemini nereden biliyor/anlıyor?
Bir makine (router veya switch), gelen paketin BGP olduğunu paketin içindeki katmanlı başlık (header) bilgilerine bakarak anlar. Bu süreç bir mektup zarfını açmaya benzetilebilir. Makine her katmanda bir sonra ki adımın ne olduğunu söyleyen bir "etiket" görür:

1. **Katman 2 (Ethernet)** - _"İçeride ne var?"_ Kablo üzerinden gelen elektrik sinyalleri bitlere (0 ve 1) dönüşür. Makine önce en dıştaki Ethernet Başlığına bakar. Burada **"EtherType"** adı verilen 2 bytelık bir alan vardır. Eğer burada `0x0800` yazıyorsa, makine şunu anlar: _"Tamam, bu paketin içinde ki bir sonra ki katman IPv4 protokolüdür."_
2. **Katman 3 (IP)** - _"Hangi ulaşım yolu?"_ Makine şimdi IP başlığını okur. IP başlığının içinde **"Protocol"** adında bir alan bulunur. Eğer burada `6` yazıyorsa, makine şunu anlar: _"Bu IP paketinin içinde TCP verisi taşınıyor."_
3. **Katman 4 (TCP)** - _"Hangi uygulama?"_ Şimdi makine TCP başlığına odaklanır. TCP katmanında en kritik bilgi **Port** Numarasıdır. Eğer **"Destination Port" (Hedef Port)** kısmında `179` yazıyorsa, makine kesin olarak şunu söyler: _"Bu paket BGP protokolüne ait bir mesajdır!"_
4. **Yazılıma Teslim (Uygulama Katmanı)** - Makine paketin BGP olduğunu anladığında, onu işletim sistemindeki (örneğin FRR, Cisco IOS, Junos) BGP servisine (daemon) yönlendirir. BGP servisi paketi açar ve içindeki **"Update", "Keepalive"** veya **"Open"** gibi mesajları okuyup işlemine başlar.

EVPN durumunda ne oluyor? BGP EVPN kullanırken işler bir tık daha detaylanır. Makine paketin BGP (Port 179) olduğunu anladıktan sonra, BGP mesajının içine bakar. BGP'nin içinde **AFI (Address Family Identifier)** ve **SAFI (Subsequent AFI)** denilen belirteçler vardır:

- **AFI 25:**  _"Ben L2VPN (Layer 2 VPN) bilgisi taşıyorum."_
- **SAFI 70:** _"Ve bu bilgi özellikle EVPN formatındadır."_

Makine bu kodları gördüğünde, gelen bilginin sıradan bir internet rotası olmadığını, senin VXLAN yapınla ilgili bir MAC adresi güncellemesi olduğunu anlar ve onu EVPN tablosuna işler. Özetle Makine;

1. Ethernet başlığına bakar: _"İçeride IP mi var?"_ -> Evet.
2. IP başlığına bakar: _"İçeride TCP mi var?"_ -> Evet.
3. TCP başlığına bakar: _"Port 179 mu?"_ -> Evet.
4. Karar: _"O zaman bu bir BGP paketidir, BGP protokol kurallarını uygula."_

Eğer port `179` değil de `80` olsaydı, makine _"BGP protokolü uygulanacaktır"_ demez, _"Bu bir web trafiğidir (HTTP)"_ derdi. Yani her şey paketin üzerine basılmış bu standart **"etiketler"** (portlar ve protokol numaraları) üzerinde ve sayesinde yürür.

#### Özetle bir protokolün işlenmesi için bir program, arkaplan programı, servis (daemon) tasarlanması mı gerekli? Örneğin C ile bir protokol tasarlanabilir mi? Paketin işlenmesi cihazın paketi servise yönlendirmesiyle oluyorsa paketlenmesi de aynı yerden mi oluyor?

Bir protokol, özünde çalışan bir koddur. Eğer bir program (daemon/servis) yoksa, protokol sadece kağıt üzerinde bir taslak olarak kalır. C ile bir protokol tasarlanabilir mi? Evet. Hatta bugün kullandığın BGP (FRR veya Quagga gibi yazılımlar), OSPF, ve TCP/IP yığınlarının neredeyse tamamı C ile yazılmıştır. C ile bir protokol yazmak için şunları yaparsın:

- **Struct (Yapı) Tanımlarsın:** Paketin başlıklarını (Header) C'deki `struct` yapılarıyla oluşturursun. Örneğin, BGP'nin **"Marker", "Length"** ve **"Type"** alanlarını temsil eden bir struct yazarsın.
- **Socket Programming:** İşletim sisteminden **"Raw Socket"** açarak, paketi hiçbir işleme uğramadan ham bir şekilde ağ kartına göndermeyi veya oradan okumayı sağlarsın.
- **Döngü (Event Loop):** Arka planda sürekli çalışan bir `while(1)` döngüsü kurarsın; bu döngü port `179`'u dinler, paket gelince onu senin yazdığın fonksiyonlara gönderir.

Paketleme ve çözme aynı yerden mi olur? Evet, genellikle aynı Daemon (Servis) bu işin her iki ucundadır. Bu sürece ağ dünyasında encapsulation (Paketleme) ve decapsulation (Paketi Açma) denir.
- **Paketleme (Giden Trafik):** Örneğin BGP servisin bir komşusuna _"Ben buradayım"_ (Keepalive) demek istiyor. Servis, C kodunda ilgili struct'ı doldurur, bellekte bir buffer oluşturur ve bunu ağ kartına (Kernel üzerinden) gönderir.
- **Çözme (Gelen Trafik):** Karşıdan bir paket geldiğinde, cihaz (Kernel) port numarasına bakıp _"Bu BGP'ye ait"_ der ve paketi senin BGP servisine teslim eder. Servisin içinde ki kod, tekrar C struct yapısına dönüştürür ve içindeki mesajı okur.

Neden _"Daemon/Servis"_ tasarlanmalı? Ağı sürekli izleyen ve onunla iletişimde olması gereken bir şeyin olması gereklidir. Bu yüzden daemon/servis şeklinde arkaplanda çalışacak bir program olarak tasarlanmalıdır.

#### Soket programlama kütüphaneleri ağ kartını nasıl programlayabileceğinin hazır kaynakları mı oluyor? Bir C soket programlama kütüphanesi aslında kernel'in ağ kartına nasıl müdahele etmesi gerektiğinin ifadesi mi oluyor?

C dilindeki soket programlama ve onun kütüphane kaynakları, kernel ile ağ kartı donanımının nasıl davranması gerektiğinin ifadesidir. Soket kütüphanesi bir **"Tercüman"dır.** Yazılan C kodu doğrudan ağ kartındaki (NIC) transistörleri yönetmez. Ağ kartı çok hızlıdır ve karmaşıktır; ona doğrudan müdahale etmek yerine, Kernel çevirmenlik yapar. Soket kütüphanesi (`sys/socket.h` gibi) sana şunları sağlar; _"Ağ kartı Intel mi, Realtek mi?"_ diye düşünülmeye gerek kalmaz. Sadece `socket()` fonksiyonunu çağırırsın. `send()` komutu verildiğinde, aslında Kernel'e şu denir örnek olarak: _"Benim elimde bir veri yapısı (struct) var. Bunu BGP protokol kurallarına göre paketle ve ağ kartı üzerinden dışarı fırlat."_

Kernel ve ağ kartı ilişkisinde "müdahele" olarak ifade edilen şey aslinda **Sistem Çağrılarıdır;**

- **Kod (User Space):** _"Soket aç, port 179'u dinle."_
- **Soket Kütüphanesi:** Bu isteği işlemcinin anlayacağı bir "Interrupt" (yarıda kesme) sinyaline dönüştürür.
- **Kernel (Kernel Space):** Bu sinyali alır, _"Tamam, kullanıcı BGP konuşmak istiyor"_ der. Kartın Driver'ına (Sürücü) talimat gönderir.
- **Ağ Kartı (Hardware):** Driver'dan gelen veriyi alır ve fiziksel kabloya elektrik sinyali olarak bırakır.

Protokol tasarlarken neyi programlıyoruz? Eğer sıfırdan bir protokol tasarlanıyorsa, aslında Kernel'e şunların nasıl yapılacağı tarif edilir:

1. **Paketin Yapısı:** _"İlk 2 byte her zaman 'Mesaj Tipi' olsun."_ (Bu C `struct`ı şeklinde yazılmış olabilir).
2. **Hata Kontrolü:** _"Eğer karşıdan 30 saniye boyunca 'Keepalive' gelmezse bağlantıyı kopar."_ (Bu `while` döngüsü olarak yazılmış olabilir).
3. **Yönlendirme:** _"Eğer gelen pakette EVPN Type-2 yazıyorsa, içindeki MAC adresini al ve tablodaki şu satıra yaz."_ (`if-else` şeklinde yazılmış olabilir).

#### Madem bir protokol cihazin ardında çalışan arkaplan servisi o halde TCP veya UDP için bir makine de _udpd_ veya _tcpd_ diye niye bir servis yok?

TCP, UDP, BGP hepsi protokol ama farklı katmanlarda çalışıyorlar. OSI modeli hatırlanacak olursa;

```
Layer 7 → Uygulama (HTTP, BGP, OSPF)
Layer 4 → Transport (TCP, UDP)
Layer 3 → Ağ (IP)
Layer 2 → Veri bağlantısı (Ethernet, MAC)
Layer 1 → Fiziksel (kablo)
```

**TCP ve UDP** → **Layer 4'te** çalışıyor. Veriyi nasıl taşıyacağını belirliyor. **BGP → Layer 7'de** çalışıyor. Ama taşınmak için TCP kullanıyor yani BGP mesajları TCP paketlerinin içinde gidiyor.

```
BGP mesajı
    ↓
TCP paketine sarılıyor (port 179)
    ↓
IP paketine sarılıyor
    ↓
Ethernet frame'ine sarılıyor
    ↓
Fiziksel kablo
```

Yani BGP bir uygulama protokolü. Routing bilgilerini taşımak için tasarlanmış. TCP veya UDP ise bir taşıma protokolü. BGP'nin güvenli iletilmesi için kullanılıyor.

### BGP ve EVPN ayrı kavramlarsa VXLAN flood sorunu için mi geliştirilmişler yoksa bunlar genel bir teknik ama bu sorunu da çözebilecek mahiyette teknikler mi? Flood sorunu olmadan evvel bu teknik veya kavramlar var mıydı? Yoksa flood sorunu üzerine geliştirilmiş teknikler mi?

**BGP** vardı ve eski bir protokoldü; ancak **EVPN**, tam olarak **"flood"** (BUM trafiği) ve ölçeklenebilirlik sorunlarını çözmek için BGP'nin üzerine inşa edilmiş yeni bir **BGP "uzantısı" (extension)** olarak doğdu. AS'ler arası routing protokolü.

**Klasik BGP (Border Gateway Protocol)**
İnternetin ana protokolüdür. 1980'lerden beri var. İlk görevi sadece **Layer 3 (IP) rotalarını** taşımaktı. Yani _"X IP adresine gitmek için şu yolu izle"_ derdi. Başlangıçta BGP sadece şunu yapıyordu: _"Ben AS 1'im ve şu IPv4 adres bloklarına sahibim"_ diye diğer AS'lere duyurmak. İnternet bu BGP duyurularından oluşuyor. Bir internet servis sağlayıcısı da AS olduğuna göre diğer ISS'lerle iletişim için bu protokol kullanılıyor. Bir bilgisayar Google'a bağlanabiliyorsa bu BGP sayesindedir. Router'lar Google'ın IP bloğunun hangi AS'te olduğunu BGP'den öğreniyor. Yani **sıradan BGP = AS'ler arası IPv4 rota duyurusu**. İnternetin omurgası BGP. Dünyada yaklaşık 70.000'den fazla AS var ve hepsi BGP ile birbirine bağlı. Senin paketi Google'a ulaştıran yol boyunca onlarca AS geçiyor. BGP'yi OSPF'e benzetebiliriz ancak BGP'de rota hesaplama OSPF'ten tamamen farklı. **OSPF → en kısa yolu** hesaplıyor. Matematiksel, objektif. **BGP → politik (ticari) olarak en iyi yolu hesaplıyor** ama "en iyi" çok faktöre bağlı:

```
AS path uzunluğu  → kaç AS'ten geçiyor
Local preference  → bu yolu ne kadar tercih ediyorum
MED               → komşuya "benden şu yoldan gir" demek
Community         → rota etiketleme
Ticari ilişki     → transit mi, peer mi?
```

Gerçek hayatta bir paket en kısa fiziksel yoldan gitmeyebilir. Turkcell _"bu trafiği Frankfurt'taki ortağımdan geçireyim"_ diyebilir — fiziksel olarak daha uzun ama ticari olarak daha avantajlı. Bu yüzden bazen Türkiye'den Türkiye'ye giden bir paket Frankfurt veya Londra'dan dönüyor politik rota kararı. Örnegin Turkcell Google'a BGP ile bağlanmak istediğinde şunlar gerekiyor:

1. **Fiziksel bağlantı** — önce fiziksel olarak bağlı olmaları lazım. Bu genellikle **IXP (Internet Exchange Point)** denilen noktalarda oluyor. İstanbul'da **TurkIX** böyle bir nokta — farklı AS'ler burada fiziksel olarak buluşuyor.
2. **BGP yapılandırması**;

```
# Turkcell router'ında:
router bgp 9121
neighbor 195.x.x.x remote-as 15169  ← Google'ın IP'si ve AS'i
```

```
# Google'ın router'ında da:
router bgp 15169
neighbor 81.x.x.x remote-as 9121  ← Turkcell'in IP'si ve AS'i
```

3. **Ticari anlaşma** — teknik kısım bu kadar basit aslında. Asıl mesele ticari anlaşma — kim kimin trafiğini taşıyacak, karşılığında ne ödeyecek. Pratikte bu bağlantıyı kurabilmek için fiziksel altyapı ve ticari anlaşma gerekiyor.

**MP-BGP (Multi Protocol BGP)**
BGP'yi özel kılan şey, **MP-BGP (Multi-Protocol BGP)** haline gelebilmesidir. Yani BGP'ye _"Sadece IP değil, başka bilgiler de taşı"_ diyebiliyoruz. Sıradan BGP önceden yalnızca tek protokol ile çalışabildiğinden yalnızca IP rota bilgilerini taşıyabiliyordu. Ancak MP-BGP ile BGP'nin taşıyabildiği adres bilgisi genişletildi. MP-BGP ile BGP artık **IPv6, VPN bilgisi, MAC adresleri** gibi farklı türde bilgileri de taşıyabiliyor. EVPN tam da bu esnekliği kullanıyor. Buna müteakip **EVPN MP-BGP'nin bir uzantısıdır.** Gerçek hayatta kullanım örnekleri:

- İnternet servis sağlayıcıları **sıradan BGP** kullanıyor — _"ben şu IP bloklarına sahibim"_ duyurusu.
- Büyük şirketler **L3 VPN için MP-BGP** kullanıyor — farklı şehirlerdeki ofisler arasında özel ağ.
- Veri merkezleri **L2 EVPN için MP-BGP** kullanıyor — iç ağ yapısında kullanilan teknik bizim projede yaptığımız şey.

**EVPN (Ethernet VPN)**
**EVPN** ise çok daha genç bir tekniktir (2010'ların başı). VXLAN ve benzeri teknolojilerle birlikte, veri merkezleri devasa boyutlara ulaştığında ortaya çıkan "flood" sorununa bir çözüm olarak geliştirildi. Geleneksel Layer 2 ağlarda (VPLS gibi), bir cihazın nerede olduğunu öğrenmek için **"Flood and Learn" (sel gibi yayıl ve öğren)** kullanılıyordu. Bu da 1000'lerce cihazlık ağlara büyük yük oluşturuyordu. Ağ mühendisleri: _"Biz neden Layer 2 (MAC) bilgilerini de Layer 3 (IP) rotaları gibi önceden dağıtmıyoruz? Elimizde BGP gibi devasa verileri taşıyabilen sağlam bir protokol var, MAC adreslerini de onun içine paketleyip gönderelim."_ dendi. Klasik BGP normalde IP adreslerini (prefix) taşımak için tasarlanmıştı. EVPN (Ethernet VPN) ise BGP'ye yeni bir yetenek kazandırarak, BGP paketlerinin (Update paketleri) içerisinde MAC adreslerini (IP rota bilgilerini de) birer rota gibi taşımasını sağlayan bir aile **(Address Family)** eklentisidir. Yani sadece **EVPN + VXLAN** dendiği zaman kastedilen şey **BGP paketlerinde MAC adres bilgilerinin de barındırılmasıdır.** Bunu takiben aslında EVPN demek BGP demek ancak içerisinde klasik şekilde yalnızca IP rota bilgilerini içeren şekilde değil aynı zaman da MAC adres bilgilerini içerecek biçim de formlanmış bir **BGP formu = EVPN**. Kısaca :d BPG paketinin içinde MAC adresinin de olması ve taşınması durumuna EVPN deniliyor. Ayrıca bazı ağ topolojilerinin yapılarını ifade ederken sadece **EVPN + VXLAN** veya **EVPN + MPLS** gibi kavramlar kullanılabilir ve neden **BGP + VXLAN** değilde o şekilde kullandıldığı doğallıkla sorulabilir. Bir ağ topolojisinin yapısı hakkında açıklama yaparken _"BGP kullanıyorum"_ denilirse çok geniş — hangi adres ailesi, ne için? _"EVPN kullanıyorum"_ dersen spesifik — MAC adresleri için BGP uzantısı kullanıyorum. **BGP denilirse** → genel protokol, çok amaçlı ama **BGP EVPN denilirse** →  MAC adresi taşıyan spesifik yapılandırma. Network dünyasında kavramsal bir iç içelik durumu söz konusu olduğundan şu durumlar ortaya çıkabiliyor; Aynı şeye farklı isimler veriliyor (VTEP = PE = tunnel endpoint). Her üretici kendi terminolojisini ve literatürünü kullanıyor (Cisco vs Juniper vs Linux).

Normal bir cihaz, diğer bir cihazın nerede olduğunu anlamak için trafiğin gelmesini bekler veya her yere sorar (Flooding). EVPN'de ise durum şöyledir:

1. Bir router (VTEP/PE), kendisine bağlı bir bilgisayarın MAC adresini öğrendiği anda, bunu bir BGP Update paketine koyar.
2. Bu paketin içine _"`A0:B1:C2` MAC adresi bende, bana ulaşmak için şu IP'ye gel"_ bilgisini yazar.
3. **RR/Spine/Controller** cihazı bu bilgiyi alır ve tablosuna işler. Ardından bunu ona bağlı olan **client/leafs** cihazlarina dağıtır.
4. Ağdaki diğer tüm cihazlar bu BGP paketini alır ve kendi tablolarına işler.

Buna network literatüründe **Control-Plane Learning (Kontrol Düzlemi ile Öğrenme)** denir. Yani artık **"su baskını" (flooding)** yaparak öğrenmek zorunda değilsin; haberleşme başlamadan herkes kimin nerede olduğunu biliyor.

**BGP EVPN kombinasyonu**
EVPN aslında BGP'nin taşıdığı bir "yük" (payload) gibidir. BGP bir kamyonsa, EVPN o kamyonun içindeki özel bir kargo tipidir. 
- **Flood Öncesi Durum:** Eskiden MAC adreslerini öğrenmek için paketin her yere gitmesi (flood) şarttı. Çünkü bir **"kontrol merkezi"** yoktu. 
- **EVPN Sonrası Durum:** EVPN sayesinde artık bir VTEP, arkasına yeni bir cihaz takıldığında bunu bir BGP mesajı olarak paketler. Bu mesaja _"Type-2 Route" (MAC/IP Advertisement)_ denir. Diğer tüm VTEP'lere bu bilgiyi fısıldar. 
**Sonuç:** Artık kimsenin **"flood"** yapmasına gerek kalmaz. Çünkü her VTEP'in elinde, ağda ki her bir MAC adresinin hangi VTEP'in arkasında olduğuna dair devasa bir _"telefon rehberi"_ (BGP tablosu) oluşur. Yani EVPN, BGP'ye _"Artık sadece IP rotalarını değil, MAC adreslerini ve VXLAN bilgilerini de taşıyacaksın"_ talimatının verilmiş halidir. Yani **BGP EVPN + VXLAN** yapısının daha optimal biçimde işleyebilmesi için geliştirilmiş bir teknik/çözüm.

### RR/Spine/Controller cihazının ağda ki tüm Leaf'e bağlı host'ların MAC adreslerini öğrenme sorumluluğu/rolü flooding yöntemine nazaran tek bir merkeze yüklemek yine performams kaybı oluşturmaz mı?
Ağ RR cihazı ile birlikte ağda ki diğer cihazlarin MAC adreslerini bir kere öğrendikten sonra bunu tablosuna kaydeder. Geri kalan iş ağa yeni katılma veya ağdan düşme durumlarında buna uygun olarak tablosunu güncellemektir. Önceden sorun VTEP cihazlarının ARP ile temin ettikleri ve ARP tablosuna geçici olarak kaydettikleri MAC adres bilgilerini yeniden ve sürekli olarak aynı temin methodunu uygulamasıydı. RR cihazi bunu bir kez kendi merkezinde temin edip diğer cihazlara bunun hakkında haber maksatlı dağıtma rolünü üstlendiği anda yineleme sorununu ortadan kaldırır. Çünkü leafs'ler artık önceden MAC adreslerinin bilgisine ve rota bilgisine sahip oldugundan (RR'den aldıkları bilgileri tablolarına yazdıklarından) tek yapılmasi gereken iş veri düzleminde verinin/veri trafiğinin taşınmasi işlemidir. Bu da hızlı bir işlem olduğundan büyük oranda performans kazancı elde edilir. Özetle asıl iş paket gönderilmeye niyet edildigi zaman ağda ki hedef cihazin adres bilgisini temin etmektir. Ancak bu cihazin CPU ve diğer önemli kaynaklarını harcamak demek. İşin yorucu kısmı burada yatıyor. Ancak bir kere rota bilgisi elde edildi mi tek yapılması gereken rota bilgisi himayesinde paketi göndermektir.

Ayrıca proje de küçük bir veri merkezi topolojisi kurulduğundan zaten RR cihazı pek yorulmaz ancak 1000 veya 2000 adet Leaf durumunda zaten RR cihazi böyle bir yapı için buna uygun olarak sayısı arttırılıp konumlandırılıyor. Ve son olarak MAC adres bilgisi veri trafiğine kıyasla çok küçük bir veridir.

**AS2 (Google), AS1**'e der ki: _"`8.8.8.0/24` bloğuna ulaşmak istersen benden geç."_ AS1 bunu öğrenir ve paketleri Google'a yönlendirir. İnternette BGP farklı AS'ler arasında kullanılıyor — Turkcell ile Google gibi. Az önce ki örnekte olduğu gibi işte buna **eBGP** deniyor.  Ama BGP aynı zamanda aynı AS içinde de kullanılabiliyor — buna **iBGP** deniyor.

Yani BGP'nin 2 modu var:

1. **eBGP (External BGP)**
- Farklı AS'ler arasında konuşulur
- İnternetin omurgası
- Örnek: Kablonet (AS 1) ile Google (AS 2) arası → eBGP

2. **iBGP (Internal BGP)**
- Aynı AS içinde BGP bilgisini yaymak için
- _"Dışarıdan öğrendiğimiz rotaları içeride de paylaşalım"_
- Örnek: Kablonet (AS 1) kendi içindeki router'lar arası → iBGP

iBGP ve eBGP'nin birlikte kullanımına örnek olarak bir diyagram;

```
[AS1]────eBGP────[AS2]────eBGP────[AS3]
  │                │                │
iBGP             iBGP             iBGP
  │                │                │
router           router           router
```

Part 3'te tek bir AS var — AS numarası 1. Tüm VTEP'ler ve RR aynı AS içinde. Bu iBGP. BGP'nin AS'ler arası routing protokolü (eBGP olarak kullanılması) olması burada önemli değil — sadece MAC adreslerini taşıma özelliğini kullanıyoruz.

Ayrıca **iBGP ve OSPF** birbirlerine benzetilebilir ancak bu proje de (BADASS) ikisi farkli roller üstlenir;

- **OSPF** → _"Bu ağda hangi IP'lere nasıl ulaşırım?"_ sorusunu çözüyor. Yani routing tablosunu dolduruyor. Paketleri fiziksel olarak doğru yere iletmek için.
  - **OSPF**  → VTEP-1'den VTEP-4'e paket nasıl gider? (fiziksel yol)
- **iBGP** → _"Bu ağda hangi servisler, hangi MAC'ler, hangi VPN'ler var?"_ sorusunu çözüyor. Routing tablosundan çok bilgi dağıtımı yapıyor.
  - **iBGP**   → VTEP-4'teki Host'un MAC adresi nedir? (servis bilgisi)

İkisi birbirini tamamlıyor. BGP _"Host şu VTEP'te"_ diyor ama paketi oraya nasıl göndereceğini bilmiyor — OSPF'e soruyor. OSPF'de rotayı bildiğinden paket ulaştırılabiliyor.

Yani;
**BGP**  → nerede olduğunu biliyor
**OSPF** → oraya nasıl gidileceğini biliyor

_"OSPF MAC öğrenemiyor mu?"_ diye bir soru yöneltilebilir; Hayır. OSPF sadece IP adresleri ve ağ yollarıyla ilgileniyor — MAC adresi onun dünyasında yok. OSPF Layer 3 protokolü — IP seviyesinde çalışıyor. MAC adresi ise Layer 2. OSPF'e _"şu MAC adresi şu VTEP'te"_ diyemiyorsun çünkü OSPF bu bilgiyi taşıyacak kapasitede tasarlanmamış. BGP ise çok esnek — **MP-BGP** ile IP rotaları, MAC adresleri, VPN bilgileri gibi farklı türde bilgileri taşıyabiliyor. EVPN tam bu esnekliği kullanıyor. OSPF MAC adresi taşıyamasa da BGP OSPF'in yaptığı işi yapabilir ancak OSPF kadar hızlı değil (yani underlay ağ için IP rotası keşfetme işi). BGP için _"IP rotaları taşıyabiliyor"_ tanımı doğrudur. BGP de tıpkı OSPF gibi IP rotalarını taşıyan dinamik bir yönlendirme protokolüdür. Ancak ikisinin **underlay** ağında rotaları keşfetme ve komşuluk kurma yöntemleri arasında çok kritik bir fark vardır. OSPF'in underlay ağlarda daha çok tercih edilmesinin nedeni **"tak-çalıştır"** (plug-and-play) mantığına sahip olmasıdır. BGP ise geleneksel olarak daha temkinli ve manuel konfigürasyon gerektiren bir yapıya sahiptir. Ama teknik olarak ikisi de IP prefix/route taşır. İkisi de komşularından rota öğrenir ve routing table’a yazar. Fark şurada; **OSPF = link-state IGP'dir**. Ancak **BGP = path-vector protocol**

Yani çalışma mantıkları farklıdır, ama ikisi de underlay routing yapabilir.

- **OSPF (Otomatik Keşif):** OSPF, multicast (`224.0.0.5`) paketleri göndererek ağdaki diğer OSPF cihazlarını otomatik olarak keşfeder. Komşu cihazın IP adresini önceden bilmene gerek yoktur. Komşuluk kurulduktan sonra tüm IP rotaları otomatik olarak senkronize edilir.
- **Klasik BGP (Manuel Eşleşme):** BGP, güvenliğe ve kontrole odaklanır. Daha hantaldır.
### PDF'de belirtilen _"dynamic relationship"_ ifadesi ve _"IP atamadan MAC adresini keşfetme"_ vurguları
Veri merkezlerinde yüzlerce router olduğu düşünüldüğünde, her yeni router eklendiğinde mevcut tüm cihazlara girip tek tek yeni IP'yi RR'de tanımlamak zorlaştırıcı bir pratiktir. PDF'de buna vurgu yapılmasının sebebi bu dur. Part-2'de ki multicast özelliğinin kolaylaştırıcı etkisi benzeri bir konfigürasyonu da burada ki aynı durum için uyarlanması isteniyor. Yani BGP'de ki komşuluk ilişkilerini de dinamikleştirebiliyoruz. **Dynamic Relationships** tam bu noktada devreye giriyor. Leaf (VTEP) cihazlarının IP adreslerini merkezi RR cihazına tek tek statik olarak tanımlamak yerine, RR üzerinde **dinamik komşuluk (Dynamic BGP Neighbors / Listen Range)** özelliğini aktifleştiriyorsun. Bu yazıda ki egzersiz de BGP EVPN yapılandırması **static relationship** üzerinden yapıldı ancak PDF bunu istemiyor.

```
Statik → RR'de her VTEP için elle neighbor yazıyorsun
         Yeni VTEP eklenince RR'ye girip yeni neighbor ekliyorsun

Dinamik → RR'de sadece IP bloğu tanımlıyorsun
          Yeni VTEP eklenince RR'ye dokunmuyorsun
          VTEP otomatik kabul ediliyor
```

Yani dinamik ilişkinin çözdüğü sorun: Ölçeklenebilirlik. 100 VTEP'li bir ağda her yeni VTEP için RR'ye girip yapılandırma yapmak yerine, VTEP kendi kendine RR'ye bağlanıyor. VTEP'in kendi lokal yapılandırmaları dışında tabii yani; her yeni VTEP (Leaf) cihazına gidip onun kendi konfigürasyonunu manuel olarak yapmak zorundayız. Çünkü o cihaz ağa yeni katılıyor ve onun dünyadan haberi yok; kendi IP'sini alması, OSPF'e katılması ve EVPN paketlerini göndermesi ve alması konfügürasyonlarını ayarlamak gerekiyor. Network dünyasında buna **"Local Provisioning"** (Lokal Yapılandırma) denir.

Özetle;

**"Dynamic relationship"** ifadesi **BGP dynamic neighbors / listen range** özelliğini kastediyor. Yani RR'de her VTEP için tek tek `neighbor X.X.X.X remote-as 1` yazmak yerine:

```
bgp listen range 1.1.1.0/24 peer-group VTEP-GROUP
```

gibi bir komutla _"bu IP bloğundan gelen BGP isteklerini otomatik kabul et"_ diyorsun.

**Klasik (Statik) Yöntemde Ne Oldu?**
Eğer dinamik ilişki kullanılmazsa, ağa 5. veya 6. bir VTEP eklemek istediğinde şu adımların yapılması gerekirdi:
- Yeni VTEP'e git: lokal ayarlarını yap.
- Merkezi RR cihazına git: `neighbor 1.1.1.2 remote-as 1` gibi yeni VTEP'in IP'sini manuel olarak tek tek ekle. Ayrıca bunu `address-family l2vpn evpn` altında da aktifleştir.
Bu durum, ağ büyüdükçe merkezdeki (RR) ana yönlendiricinin konfigürasyonunun sürekli değiştirilmesini, dolayısıyla insan hatası riskini (yanlışlıkla tüm ağı etkileyecek bir komut yazma riski) doğurur.

**Dinamik Yöntemde Ne Oluyor?**
Dinamik ilişki kurduğunda:
- Merkezi RR cihazına dokunmuyorsun. O bir kere kuruluyor ve `1.1.1.0/24` aralığını dinlemeye başlıyor. Konfigürasyonu sabit kalıyor.
- Yeni VTEP'e gidiyorsun: Sadece o cihazın kendi lokal ayarlarını (IP, OSPF ve RR'ın IP'sini gösterme) yapıyorsun.
- Yeni VTEP, RR'a doğru bir istek gönderdiği an RR onu otomatik olarak tanıyor, elini sıkıyor (dynamic neighbor kabul ediyor) ve onu hemen EVPN ağının bir parçası yapıyor.

Bu yüzden BGP EVPN yapısı **dynamic relationship** olarak kurulacaksa şu şekilde işlemler yapılmalıdır;

RR'de;
```
vtysh
configure terminal
router bgp 1
neighbor VTEP-GROUP peer-group
neighbor VTEP-GROUP remote-as 1
neighbor VTEP-GROUP update-source lo
bgp listen range 1.1.1.0/24 peer-group VTEP-GROUP
!
address-family l2vpn evpn
neighbor VTEP-GROUP activate
neighbor VTEP-GROUP route-reflector-client
exit
exit
exit
write
```


- `neighbor VTEP-GROUP peer-group` -- _"`VTEP-GROUP` adında bir komşu grubu oluştur"_ demek. Tek tek her VTEP için ayrı komut yazmak yerine hepsini bir grupta topluyoruz. Gruba yapılan ayar tüm üyelere uygulanıyor.
- `neighbor VTEP-GROUP remote-as 1`-- _"Bu gruptaki tüm komşular AS 1'de"_ demek. Yani gruba katılan her VTEP iBGP komşusu olacak.
- `neighbor VTEP-GROUP update-source lo` -- _"Bu grupta ki komşularla loopback üzerinden konuş"_ demek. Daha önce tek tek her komşu için yazıyorduk, şimdi gruba yazıyoruz.
- `bgp listen range 1.1.1.0/24 peer-group VTEP-GROUP` -- En kritik komut bu. _"`1.1.1.0/24` bloğundan gelen BGP komşuluk isteklerini otomatik kabul et ve `VTEP-GROUP` grubuna ekle"_ demek. Yani yeni bir VTEP eklendiğinde — loopback IP'si `1.1.1.0/24` bloğunda olduğu sürece — RR'ye dokunmadan otomatik kabul ediliyor.
- `neighbor VTEP-GROUP activate` ve `route-reflector-client` -- Grubun tüm üyeleri için EVPN aktif ve hepsi RR client'ı.

VTEP'ler de yapılması gereken BGP ayarları;
```
vtysh
configure terminal
router bgp 1
neighbor 1.1.1.1 remote-as 1
neighbor 1.1.1.1 update-source lo
!
address-family l2vpn evpn
neighbor 1.1.1.1 activate
advertise-all-vni
exit
exit
exit
write
```

Daha önceden de belirtildiği üzere VTEP'lerde ki bu konfigurasyonlar hem VTEP'in nasıl ve hangi ortama gireceği hakkında kendisini bilgilendiriyor hem de RR'ın bundan otomatik olarak haberi olup ekstra onun BGP yapılandırmasında bu VTEP'in IP'sini tanımlamıyoruz. Bu yapılandırmaların ardından RR'de `show bgp summary` komutu ile dinamik ilişkilerin kurulup kurulmadığı teyit edilebilir;

Tabloda `* - dynamic neighbor` — yıldız işareti VTEP-1'in dinamik olarak kabul edildiğini gösteriyor. RR'ye dokunmadan otomatik bağlandı.

_"IP atanmadan MAC öğrenme"_ ne demek?
PDF'te bizzat _"without assigning an IP address our VTEP automatically discovers the MAC address (IP adresi atanmadan VTEP otomatik olarak MAC adresini keşfeder)"_ ifadesi yer alıyor. Bir Leaf cihazının, altındaki host'u BGP EVPN ile ağa duyurabilmesi için (Route Type 2 oluşturması için) o host'un varlığından ilk kez haberdar olması gerekir. Leaf cihazı (FRR/Zebra), durup dururken host'a _"orada kimse var mı?"_ diye `ping` atmaz veya onu taramaz. Host'un kabloya en az bir kez dokunmasını bekler. PDF yazarının ortamında IP atanmadığı halde ne oluyor? Modern Linux çekirdekleri (ve bazı Docker imajları), ağ arayüzü (interface) **"UP"** duruma getirildiği an, daha üzerinde hiçbir IPv4 adresi tanımlanmamış olsa bile yerel ağa otomatik olarak **IPv6 Link-Local paketleri (DAD - Duplicate Address Detection) veya Gratuitous ARP (GARP)** paketleri fırlatır. Bunlar işletim sisteminin ağa dahil olurken kendi kendine yaptığı otomatik bülten yayınlarıdır. Bu paket yerel kablodan geçip Leaf cihazına ulaştığı an, Leaf cihazı paketin içeriğinde ki **"Source MAC"** kısmından host'un MAC adresini bulur. IP adresi olmasa bile sadece MAC adresini içeren bir Route Type 2 (MAC-only) rotası üretip RR'a gönderir. PDF yazarının ekran görüntüsünde **IP atanmadan tablonun dolması** tamamen bu otomatik işletim sistemi paketleri sayesindedir. Ayrıca BGP EVPN'in özelliğinin de katkısı var. EVPN'de VTEP, host'un MAC adresini IP adresi olmadan da öğrenip BGP üzerinden duyurabiliyor. PDF'te bunu gösteriyor — host çalışır duruma gelince VTEP onun MAC adresini otomatik öğreniyor, IP ataması yapılmasa bile.
### BGP EVPN tablosunda keşfedilmiş MAC adreslerinin bir süre sonra tablodan gitmesi üzerine
VTEP bu MAC adresini bridge tablosunda tutuyor. Bridge tablosunun ageing time'ı var — tıpkı daha önce `brctl showmacs br0'da` gördüğümüz gibi. Belirli süre trafik gelmezse bridge tablosundan siliniyor. MAC bridge tablosundan silinince VTEP _"bu MAC artık yok"_ diye **BGP withdraw** mesajı gönderiyor — RR'de tablodan siliyor. VTEP cihazı MAC adresini bridge tablosundan öğreniyor. Bridge, host'tan gelen trafiği izleyerek _"bu MAC adresi bu port'tan geliyor"_ diye tabloya yazıyor. BGP EVPN ise bu bilgiyi dışarıya duyuruyor — _"bridge tablomda şu MAC adresi var"_ diyor.

```
Host trafik gönderir
        ↓
Bridge tablosuna MAC eklenir
        ↓
VTEP bunu fark eder → BGP EVPN ile duyurur
        ↓
RR tabloya yazar, diğer VTEP'lere dağıtır
```

Bridge tablosu ageing time'ı dolunca ve MAC'i silince:

```
Bridge tablosundan MAC silindi
        ↓
VTEP "bu MAC artık bende yok" fark eder
        ↓
BGP withdraw mesajı gönderir
        ↓
RR tablodan siler, diğer VTEP'lere bildirir
```

#### BGP EVPN neden bridge tablosuna bağımlı?
Çünkü VTEP _"bu MAC bende var"_ diyebilmek için gerçekten o MAC'i görmüş olması gerekiyor. Bridge tablosu bu görme işlemini yapıyor — fiziksel kanıt. BGP EVPN sadece bu bilgiyi taşıyan kurye — bilginin kaynağı bridge tablosu. VTEP _"Host-1'in MAC adresi bende"_ diye BGP üzerinden duyuruyor. Ama bunu söyleyebilmesi için gerçekten Host-1'den bir paket görmüş olması lazım — yoksa yanlış bilgi duyurmuş olur. Bridge tablosu bu _"gerçekten gördüm"_ kanıtını tutuyor. BGP EVPN'in MAC adresini öğrenebilmesi için o MAC adresinin bir yerden gelmesi lazım. BGP EVPN kendi başına MAC adresi üretemez veya keşfedemez. İki seçenek var:

1. **Veri düzleminden öğren (bridge)**
Host paket gönderir → bridge yakalar → MAC tabloya girer → BGP duyurur.

2. **Kontrol düzleminden öğren**
ARP proxy gibi mekanizmalar — ama bunlar da sonunda fiziksel bir kaynağa dayanmak zorunda.

BGP EVPN sadece bir taşıyıcı — MAC bilgisini bir VTEP'ten alıp diğerlerine götürüyor. Ama o bilginin kaynağı fiziksel olarak host'un bağlı olduğu VTEP'teki bridge tablosu. BGP EVPN bridge tablosuna bağımlı çünkü MAC adreslerini kendisi keşfedemiyor — keşif işi bridge'in görevi, dağıtım işi BGP EVPN'in görevi. İkisi birbirini tamamlıyor — bu yapı için biri olmadan diğeri eksik kalıyor.

```
Bridge tablosu → MAC adresini keşfeder
BGP EVPN       → MAC adresini dağıtır
```

```
Host-1 paket gönderdi → bridge "bu MAC bu porttan geldi" diye tabloya yazdı
                               ↓
                     VTEP bu kaydı görüyor
                               ↓
               "Ben bu MAC'i gerçekten gördüm, duyurabilirim" diyor
                               ↓
                     BGP EVPN ile duyuruyor
```

Yani bridge tablosundaki kayıt _"ben bu cihazı gördüm, aktif"_ demek. Kayıt silinince _"artık bu cihazı göremiyorum, gitti"_ demek.

#### Host'un pasif duruma düşmemesi için ağ içinde sürekli ayakta kalabilmesi için çözümler nelerdir?

Host sürekli trafik üretmeli veya ARP proxy gibi mekanizmalar devreye girmeli. Gerçek veri merkezlerinde bu sorun **ARP supression ve GARP (Gratuitous ARP)** ile çözülüyor — host periyodik olarak _"ben hâlâ buradayım"_ diye ARP gönderiyor.

```
Host başladı → otomatik ARP gönderdi → MAC tabloya girdi
Sessiz kaldı → ageing time doldu → bridge tablosundan silindi
             → BGP withdraw → RR tablosundan silindi
```

Peki gerçek hayatta bu sorun nasıl çözülüyor? Host sürekli trafik üretmek zorunda mı?
Hayır. İki çözüm var:
1. **ARP supression**
VTEP host adına ARP cevapları veriyor. Host sessiz kalsa bile VTEP _"bu MAC bende"_ diye devam ediyor.
2. **Periyodik GARP (Gratuitous ARP)**
Host belirli aralıklarla _"ben hâlâ buradayım"_ diye otomatik ARP gönderiyor. Linux'ta bu arping veya kernel ayarlarıyla yapılabiliyor.
Bizim basit Alpine container'ımız bu mekanizmaları otomatik yapmıyor — bu yüzden sessiz kalınca MAC siliniyor. Gerçek veri merkezlerinde kullanılan Linux dağıtımları veya hypervisor'lar bu mekanizmaları otomatik hallediyor.

### ARP proxy ve benzeri teknikler ile ağ cihazları (host'lar vb.) canlı tutulabiliyorsa bu durumda ARP ve MAC tablolarında ki ageing time süresi hiçbir zaman dolmaz. Dolmazsa da kalan iş sadece veriyi göndermek olur (veri trafiği). Böyle bir teknik uygulanabiliyorsa BGP EVPN gibi çözümlere neden ihtiyaç var?

Temel varsayım _"Her cihaz sürekli aktif → ageing time dolmaz → flood gerekmez -> flood'a bile gerek kalmazsa BGP EVPN'e hiç gerek kalmaz"_ Bu varsayımda kaçırılan bir noktanın vurgulanması gerekiyor. Veri merkezlerinin ağ altyapılarında statik bir yapı yok;

**1. Sanal Makine Göçü (Live Migration)**
Bulut altyapısında bir VM (sanal makine) bir fiziksel sunucudan başka birine anlık taşınıyor. Yani:
```
VM-1 eskiden VTEP-2'nin arkasındaydı
        ↓
Şimdi VTEP-7'nin arkasına taşındı
```
Tüm ağ _"VM-1'in MAC adresi artık VTEP-7'de"_ diye güncellenmesi gerekiyor. Anında. Flood ile bunu nasıl yapacaksın?

**2. Yeni Sunucu / Cihaz Ekleme**
Veri merkezine yeni bir rack geldi, 50 yeni sunucu eklendi. Bunların MAC adresleri hiçbir VTEP'te yok. İlk iletişimde flood kaçınılmaz.

**3. Ağ Bölümlenmesi (Network Partition)**
Bir switch veya link çöktü. VTEP'ler birbirinden geçici olarak koptu. Tablolar silindi. Tekrar bağlanınca her şey yeniden öğrenilmek zorunda.

**4. Binlerce Eş Zamanlı Değişiklik**
Amazon veya Google ölçeğinde binlerce VM aynı anda başlıyor, duruyor, taşınıyor. Her biri flood üretirse ağ çöker.

**BGP EVPN'in Asıl Farkı**

Flood ile öğrenme → _"bekle, paket gelsin, o zaman öğren"_
BGP EVPN → _"paket gelmeden önce haber ver"_

VM taşındığı anda VTEP-7 hemen BGP EVPN ile _"VM-1 artık bende"_ diye duyuruyor. Tüm ağ flood olmadan güncelleniyor. Bu senaryo küçük ve statik ağlar için geçerli olabilir. Örneğin proje topolojisinde böyle mini bir veri merkezi kurduğumuzdan bu yanılgıya sürekli düşmek normal. Ama veri merkezi dinamik bir yapı — sürekli değişiyor. BGP EVPN bu dinamizmi flood olmadan yönetmek için var.
### Bir host'un MAC adresinin BGP EVPN tablosuna kaydedilebilmesinin bir yolu da `ping` atmakdır. Kısaca bu yolla ağda aktif olduğunu göstermek. Ancak bu ARP trafiği oluşturmak demek oluyor. Biz BGP EVPN'i zaten tam da bu amaçla ARP flooding'ten kurtulmak icin kullanmıyor muyduk? Yani ARP atmadan arkaplan da (kontrol düzleminde) cihazlarin birbirlerine paket göndererek (BGP paketleri) kimin ağ da kimin ağ da olmadığını sürekli kontrol eden bir mekanizma ile MAC adresleri elde edilmiyor muydu? O halde neden yine host'dan ping atilarak ARP trafiği oluşturuluyor?

BGP EVPN'in ARP Flooding sorununu çözmek için tasarlandığı fikri %100 doğru. Yanlış anlaşılan ya da gözden kaçırılan kısım, bu mekanizmanın nerede çalıştığı ve nasıl işlediğidir. Bu taşları yerine oturtmak için mimariyi ikiye ayırmamız gerekiyor: **Host ile Leaf (VTEP) arası** ve **Leaf ile Leaf arası**;

BGP EVPN host'lar üzerinde çalışmaz; BGP EVPN, uç cihazlar (Alpine host'ları) arasında çalışan bir şey değildir. Host'ların arkada dönen BGP EVPN altyapısından, Route Reflector'lardan (RR) veya VXLAN'dan zerre kadar haberi yoktur. Onlar kendilerini tamamen sıradan, düz bir fiziksel switch'e kabloyla bağlanmış bir ağ da sanırlar. Bir bilgisayarın (Host-1), başka bir bilgisayara (Host-2) paket gönderebilmesi için TCP/IP mimarisinin temel kuralı gereği karşı tarafın MAC adresini bilmesi şarttır. Host-1 normal bir bilgisayar olduğu için, ağa çıkarken her halükarda bir ARP Request (ARP İsteği) paketi üretmek zorundadır. BGP EVPN bu zorunluluğu host'un elinden alamaz. Ancak bastırabilir.

BGP EVPN ARP flooding'i nasıl engeller? (ARP Suppression/Bastırma); BGP EVPN'in işleyişi, Host-1 bu ARP isteğini fırlattıktan hemen sonra başlar;

- **Geleneksel Ağlarda (BGP EVPN Olmadan):** Host-1 bir ARP Request (Broadcast) fırlatır. Leaf-1 bu paketi alır, kimde olduğunu bilmediği için VXLAN tünelinin içine sokar ve ağdaki bütün VTEP cihazlarına FLOOD eder (yayınlar). Binlerce hostun sürekli ARP yayını yaptığını düşünürsen, omurga ağ çöker.
- **BGP EVPN altyapısıyla:** Host-1 yine lokal olarak ARP Request fırlatır. Ancak Leaf-1 bu paketi aldığında onu ağa flood etmez. Çünkü Leaf-2, kendi altında ki Host-2'nin MAC ve IP adresini BGP EVPN (Route Type 2) üzerinden arka planda kontrol düzleminde (Control Plane) Leaf-1'e çoktan fırlatmıştır (RR aracılığıyla). Leaf-1 kendi BGP tablosuna bakar: _"Host-2'nin MAC adresi bende zaten kayıtlı"_ der. ARP paketinin ağda yukarı tırmanmasını engeller (ARP Suppression / ARP Bastırma), paketi yakalar ve Host-1'e bizzat kendisi Host-2 adına cevap verir (Proxy ARP). ARP paketleri Host ile lokal Leaf arasında kalır. Omurga ağda (VTEP'ler ve RR arasında) asla tek bir ARP Flooding (yayın fırtınası) yaşanmaz. Kontrol düzleminde cihazların birbirini denetlemesi işte tam olarak bu dur; ağda ki tüm cihazların adres haritası VTEP'ler arasında BGP ile önceden paylaşılır.

### Eğer ki MAC adresleri, host cihaz pasif duruma geçtiğinde BGP EVPN tablosundan siliniyorsa bu host'un MAC adresi tekrardan nasıl öğreniliyor? Çünkü VTEP'lere host'ların MAC adresleri RR cihazi aracılığıyla yansıtılıyor ama RR cihazı da bu host'un MAC adresini bilmiyorsa ne oluyor? Yani tüm ağ tarafından artık bu host'un MAC adresi bilinmiyorsa ne oluyor tekrardan bilebilmek için?

**BGP EVPN Ingress Replication (veya Multicast)**
BGP EVPN, kontrol düzlemi (Control-Plane) tabanlı bir teknoloji olsa da, bu tür bilinmeyen (Unknown Unicast, Broadcast, Multicast - BUM) trafikleri yönetebilmek için arka planda bir veri düzlemi (Data-Plane) mekanizması barındırır. BGP EVPN kurulurken, VTEP'ler birbirlerine sadece host MAC'lerini söylemezler; **"Type 3 (IMET - Inclusive Multicast Ethernet Tag)"** denilen özel bir BGP rotası daha paylaşırlar. Bu rota şu anlama gelir: _"VTEP'ler, eğer elinizde hedefi bilinmeyen bir paket kalırsa, beni de içeren şu flood listesine bu paketi çoğaltıp gönderin."_ VTEP-1, hedefi bilmediği için paketi Ingress Replication (veya yapılandırıldıysa Multicast) mekanizmasıyla ağdaki tüm VTEP'lere kopyalayarak gönderir (Flood eder).

```
1. VTEP tabloya bakar → "bu MAC kimde? bilmiyorum"
        ↓
2. BGP EVPN'in veri düzlemi mekaniması devreye giriyor
   (Type-3 rotası)
        ↓
3. VTEP paketi Ingress Replication ile tüm VTEP'lere flood eder
        ↓
4. Hedef host'un bağlı olduğu VTEP paketi alır ve host'a iletir
        ↓
5. Host cevap verir → VTEP MAC adresini öğrenir
        ↓
6. BGP EVPN Type-2 ile RR'ye bildirir
        ↓
7. RR tüm VTEP'lere yansıtır
```

Eğer RR ve VTEP'ler bir MAC adresini unutmuşsa, sistem geçici olarak klasik VXLAN mantığına (BUM Traffic / Flood) geri döner. Paket tüm ağa yayılır, hedef cihaz cevap verip kendini belli ettiğinde, bağlı olduğu VTEP bu bilgiyi BGP ile RR'a ve tüm ağa yeniden ilan eder. Bu yüzden gerçek senaryolarda veri merkezlerinde host'ların sürekli aktif kalması veya ARP proxy mekanizmalarının kullanılması önemli. Ayrıca burada ki en temel yanılgı (veya eksik bilgi) şu dur: VTEP'ler bir yere paket gönderecekleri zaman RR (Route Reflector) cihazına _"Bu MAC adresi kimde?"_ diye danışmazlar. BGP EVPN bir DNS veya ARP sunucusu gibi çalışmaz. RR da bir veritabanı sorgu merkezi değildir. Sistem **Push** mantığıyla çalışır, **Pull (Çekme/Sorgulama)** mantığıyla değil. Yani bir host aktif olduğunda, onun MAC adresi BGP vasıtasıyla ağda ki tüm VTEP'lere önceden dağıtılır (push edilir). MAC adresi öğrenen bir VTEP önce bunu RR'ına bildirir RR'de diğer tüm cihazlara bunu dağıtır.

### OSPF, BGP vb. tüm bu yapılandırmalar için gerçek senaryolarda gerçekten tek tek her cihaza manuel konfigürasyonlar mı yapılıyor?

Gerçek hayatta bunu otomatize etmek için **Ansible/Terraform** gibi otomasyon araçları kullanılıyor;

-  **Ansible**
En yaygın kullanılan ağ otomasyonu. Bir YAML dosyasına _"şu cihazlara şu yapılandırmayı uygula"_ yazıyorsun, Ansible tüm cihazlara otomatik bağlanıp yapılandırıyor.
-  **Terraform**
Altyapıyı kod olarak tanımlıyorsun — _"şu kadar VTEP olsun, şu yapılandırmayla"_ diyorsun, Terraform bunu otomatik kuruyor.
-  **NetBox**
Ağ cihazlarının envanterini ve yapılandırmalarını yöneten bir platform. Ansible ile birlikte kullanılıyor.
-  **NAPALM**
Network Automation and Programmability Abstraction Layer — farklı üreticilerin cihazlarını aynı Python koduyla yönetmeni sağlıyor.

Özet;
```
Küçük ağ  → manuel yapılandırma
Orta ağ   → Ansible
Büyük ağ  → Terraform + Ansible + NetBox
Dev ağ    → özel platformlar (Google, Amazon kendi araçlarını yazıyor)
```
Bu araçlar ayrı bir uzmanlık alanı — Network Automation veya NetDevOps olarak adlandırılıyor.
### BGP EVPN VXLAN ile host üzerinden yola çıkan bir paketin yolculuğu ve bu yolculukta maruz kaldığı tüm durumlar ve işleyişler

#### Bir paketin ilk kez gönderileceği zaman ki yolculuğu

**Senaryo:** Host-1 (`30.1.1.1`) → Host-2 (`30.1.1.2`) ilk kez paket gönderiyor.


**1. Adım: Host-1 paket göndermek istiyor**

Host-1 _"`30.1.1.`'ye paket göndereceğim"_ diyor. Ama önce MAC adresini bilmesi lazım. ARP sorusu gönderiyor:

```
"Who has 30.1.1.2? Tell 30.1.1.1"
```

Bu **kontrol düzlemi** trafiği.

**2. Adım: ARP isteği VTEP-1'e ulaşıyor**

Host-1'in ARP paketi bridge üzerinden VTEP-1'e geliyor.

VTEP-1 iki şey yapıyor:

```
a) Host-1'in MAC adresini bridge tablosuna yazıyor
b) BGP EVPN üzerinden RR'ye bildiriyor → Type-2 prefix
```

Bu **kontrol düzlemi** işlemi.

**3. Adım: VTEP-1 ARP'a cevap verebilir mi?**

VTEP-1 RR'ye bakıyor — _"`30.1.1.2`'nin MAC adresi var mı?"_

**Eğer varsa** → ARP proxy devreye giriyor, VTEP-1 Host-2 adına cevap veriyor. Host-1 MAC adresini öğreniyor.
**Eğer yoksa** → ARP flood — tüm VTEP'lere gönderiliyor. Host-2'nin bağlı olduğu VTEP-2 cevap veriyor.

**4. Adım: VTEP-2 Host-2'nin MAC adresini öğreniyor**

ARP cevabı VTEP-2'den gelince:

```
VTEP-2 → Host-2'nin MAC adresini bridge tablosuna yazıyor
        → BGP EVPN üzerinden RR'ye bildiriyor → Type-2 prefix
        → RR bunu VTEP-1'e yansıtıyor
```

Bu **kontrol düzlemi** işlemi.

**5. Adım: Host-1 artık MAC adresini biliyor**

Host-1 "30.1.1.2'nin MAC adresi şu" öğrendi. Asıl paketi gönderiyor.

Bu **veri düzlemi** başlangıcı.

**6. Adım: VTEP-1 paketi kapsüllüyor**

Paket VTEP-1'e ulaşıyor. VTEP-1:

```
BGP EVPN tablosuna bakıyor → "30.1.1.2'nin MAC'i VTEP-2'de (1.1.1.3)"
        ↓
Paketi VXLAN ile kapsüllüyor:
[Dış IP: 1.1.1.3 | UDP: 4789 | VXLAN VNI: 10 | İç Ethernet frame]
        ↓
Paketi fiziksel ağa gönderiyor
```

Bu **veri düzlemi** işlemi.

**7. Adım: Paket RR üzerinden geçiyor**
Fiziksel topolojide `VTEP-1 → RR → VTEP-2` yolu var. RR pakete BGP gözüyle **bakmıyor** — sadece normal IP routing yapıyor, paketi VTEP-2'ye iletiyor.

Bu **veri düzlemi** — RR burada sadece bir router gibi davranıyor.

**8. Adım: VTEP-2 paketi açıyor**

VTEP-2 paketi alıyor:

```
VXLAN başlığını soyuyor
        ↓
İçindeki orijinal Ethernet frame'i çıkarıyor
        ↓
Bridge üzerinden Host-2'ye iletiyor
```

Bu **veri düzlemi** işlemi.

**9. Adım: Host-2 paketi aldı**

Host-2 paketi aldı ve cevap gönderiyor — bu sefer ters yönde aynı süreç işliyor. Ama artık her iki VTEP de MAC adreslerini biliyor — flood olmadan direkt gidiyor.

**Özet:**

```
Kontrol düzlemi işlemleri:
→ ARP (MAC öğrenme)
→ BGP EVPN Type-2 duyurusu (MAC dağıtımı)
→ RR yansıtması

Veri düzlemi işlemleri:
→ VXLAN kapsülleme (VTEP-1)
→ Fiziksel taşıma (RR üzerinden)
→ VXLAN kapsül açma (VTEP-2)
→ Host'a iletim
```

#### Bir paketin ikinci kez gönderileceği zaman ki yolculuğu

**Senaryo:** Host-1 → Host-2 paket gönderiyor, MAC adresleri BGP EVPN tablosunda mevcut.

**1. Adım: Host-1 paket göndermek istiyor**

Host-1 _"`30.1.1.2`'ye paket göndereceğim"_ diyor. MAC adresini biliyor mu?

Host-1'in **ARP tablosuna** bakıyor:

```
ARP tablosu: 30.1.1.2 → 02:42:xx:xx:xx:xx ✓ var
```

ARP sorusu **gönderilmiyor** — direkt paketi oluşturuyor.

Bu **veri düzlemi** başlangıcı — kontrol düzlemi devrede değil.

**2. Adım: Paket VTEP-1'e ulaşıyor**

Host-1'den çıkan Ethernet frame bridge üzerinden VTEP-1'e geliyor.

VTEP-1 şunu yapıyor:

```
Hedef MAC'e bakıyor: 02:42:xx:xx:xx:xx
        ↓
BGP EVPN tablosuna bakıyor:
"Bu MAC 1.1.1.3'teki VTEP-2'de" ✓
        ↓
OSPF routing tablosuna bakıyor:
"1.1.1.3'e nasıl giderim? → 10.0.0.x üzerinden"
```

Hiçbir kontrol düzlemi işlemi yok — sadece tablolara bakıyor.

**3. Adım: VTEP-1 paketi kapsüllüyor**

```
Orijinal Ethernet frame
        ↓
VXLAN başlığı ekleniyor:
[Dış IP: 1.1.1.3 | UDP: 4789 | VNI: 10 | Orijinal frame]
        ↓
Fiziksel ağa gönderiliyor
```

Bu **veri düzlemi** işlemi — çok hızlı, ASIC yapıyor.

**4. Adım: Paket RR üzerinden geçiyor**

RR pakete bakıyor:

```
Hedef IP: 1.1.1.3
Routing tablosuna bakıyor: "1.1.1.3 → eth1'den çık"
        ↓
Paketi VTEP-2'ye iletiyor
```

RR BGP veya EVPN ile ilgilenmiyor — sadece normal IP routing yapıyor. **Veri düzlemi.**

**5. Adım: VTEP-2 paketi açıyor**

```
UDP port 4789 → VXLAN paketi
        ↓
VXLAN başlığını soyuyor
VNI: 10 → br0 bridge'ine ilet
        ↓
Orijinal Ethernet frame çıkıyor
        ↓
Bridge tablosuna bakıyor: "bu MAC eth1'de"
        ↓
Host-2'ye iletiyor
```

**Veri düzlemi** — baştan sona.

**6. Adım: Host-2 paketi aldı**

Host-2 paketi aldı. Cevap gönderecekse ters yönde aynı süreç işliyor — ama artık her şey tablolarda mevcut, hiçbir keşif işlemi yok.

**Özet:**

```
Kontrol düzlemi → HİÇ devrede değil
                  MAC adresleri zaten biliniyor
                  ARP sorulmadı
                  BGP mesajı gönderilmedi

Veri düzlemi   → Her şey burada
                  VTEP-1: tabloya bak → kapsülle → gönder
                  RR: tabloya bak → ilet
                  VTEP-2: kapsülü aç → host'a ilet
```

MAC adresleri önceden bilinince kontrol düzlemi tamamen devre dışı — paket direkt veri düzleminde uçuyor. İşte BGP EVPN'in asıl performans kazancı bu.
#### Host'lara IP atanmadan ağ da ilk kez aktif duruma geldiğinde host'larda IPv6 link-local paketleri oluşturulup VTEP'lerin bunu yakalamasının ve RR aracılığıyla diğer VTEP'lere dağıtmasının yolculuğu

**Senaryo:** Host-1'e IP atanmadan ilk kez çalışır duruma geliyor.

**1. Adım: Host-1 açıldı**

Linux açılınca `eth0` arayüzü aktif oluyor. IPv6 varsayılan olarak açık — host otomatik olarak bir **link-local adres** oluşturuyor.

Link-local adres MAC adresinden türetiliyor:

```
MAC: 02:42:da:5d:50:00
        ↓
IPv6 link-local: fe80::42:daff:fe5d:5000/64
```

Bu adres `fe80::/10` bloğundan — internete çıkmaz, sadece yerel ağda geçerli. IP atamasına gerek yok, otomatik oluşuyor.

**2. Adım: Neighbor Solicitation gönderiliyor**

IPv6'da ARP'ın karşılığı **NDP (Neighbor Discovery Protocol)**. Host-1 açılınca otomatik olarak şunu gönderiyor:

```
"Ben fe80::42:daff:fe5d:5000 adresini kullanmak istiyorum,
bu adresi kullanan var mı?" → Neighbor Solicitation
```

Hedef adres: `ff02::1` — tüm IPv6 cihazlarına multicast.

Bu **kontrol düzlemi** trafiği.

**3. Adım: VTEP-1 bu paketi yakalıyor**

Paket bridge üzerinden VTEP-1'e ulaşıyor. VTEP-1 şunu yapıyor:

```
a) Host-1'in MAC adresini bridge tablosuna yazıyor
b) BGP EVPN üzerinden RR'ye bildiriyor → Type-2 prefix
```

IP adresi yok — sadece MAC adres. EVPN Type-2 prefix'i sadece MAC ile de oluşturulabiliyor:

```
[2]:[0]:[48]:[02:42:da:5d:50:00]
Next Hop: 1.1.1.2
RT:1:10 ET:8
```

**4. Adım: RR yansıtıyor**

RR bu Type-2 prefix'i alıyor ve tüm VTEP'lere dağıtıyor:

```
RR → VTEP-2: "02:42:da:5d:50:00 MAC adresi 1.1.1.2'de"
RR → VTEP-3: "02:42:da:5d:50:00 MAC adresi 1.1.1.2'de"
```

**5. Adım: Multicast Listener Report**

Host-1 aynı zamanda IPv6 multicast gruplarına katıldığını bildiriyor:

```
ff02::1  → tüm IPv6 cihazları grubu
ff02::fb → mDNS grubu (varsa)
```

Bu paketler de bridge üzerinden geçiyor — VTEP tekrar MAC adresini görüyor, bridge tablosundaki ageing time sıfırlanıyor.

**6. Adım: Router Advertisement bekleniyor**

Host-1 ağda bir IPv6 router var mı diye soruyor:

```
"ff02::2'ye Router Solicitation gönderiyorum"
        ↓
Cevap gelirse → global IPv6 adresi otomatik alabilir (SLAAC)
Cevap gelmezse → sadece link-local ile devam eder
```

Bizim topolojimizde IPv6 router yok — cevap gelmiyor. Host sadece link-local adresle devam ediyor.

**Özet:**

```
Kontrol düzlemi:
→ IPv6 link-local otomatik oluştu
→ NDP Neighbor Solicitation gönderildi
→ VTEP bridge tablosuna MAC yazdı
→ BGP EVPN Type-2 duyurusu (sadece MAC, IP yok)
→ RR tüm VTEP'lere dağıttı

Veri düzlemi:
→ Bu aşamada henüz gerçek veri trafiği yok
→ Sadece kontrol trafiği aktı
```

IP atanmadan MAC öğrenilmesinin gizi burada — IPv6 link-local mekanizması host açılınca otomatik devreye giriyor ve VTEP bu trafiği yakalayıp MAC adresini öğreniyor.
