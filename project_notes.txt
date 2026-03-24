###########################################################
#                                                         #
#                                                         #
#    ____       _      ____    _____                 _    #
#   |  _ \     / \    |  _ \  |_   _|               / |   #
#   | |_) |   / _ \   | |_) |   | |      _____      | |   #
#   |  __/   / ___ \  |  _ <    | |     |_____|     | |   #
#   |_|     /_/   \_\ |_| \_\   |_|                 |_|   #
#                                                         #
#                                                         #
###########################################################

[ SORUNLAR ]

[dynamips, software-properties-common paketleri sorunu icin;]

"software-properties-common" paketini indirme komutlarindan sil. yani onu indirme gerekli degil debian 13 icin artik

[dynmaips icin cozum kaynaklari;]

https://www.youtube.com/watch?v=SE--UqXLShg
https://jono-moss.github.io/post/-gns3-install-debian-27-09-2024/

//////////////////////////////////////////////////////////////////////////////////////////////////////

[SIP MODULE VE QT SORUNU COZUMU]

**GNS3 Debian 13 Kurulum Sorunu ve Çözümü**

**Sorun:** `pipx` ile kurulan GNS3, eksik sistem kütüphaneleri nedeniyle başlamıyordu.

**Çözüm adımları:**

1. **PyQt6'yı pipx ortamına inject et:**
```bash
pipx inject gns3-gui PyQt6
```

2. **Eksik XCB sistem kütüphanelerini kur:**
```bash
sudo apt install libxcb-cursor0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0
```

3. **GNS3'ü başlat:**
```bash
gns3
```

---

**Neden bu oldu?**
- GNS3'ün yeni sürümleri PyQt5 değil **PyQt6** gerektiriyor
- `pipx` izole ortam oluşturduğu için PyQt6'yı manuel inject etmek gerekiyor
- Debian 13 minimal kurulumda PyQt6'nın ihtiyaç duyduğu **XCB kütüphaneleri** varsayılan olarak gelmiyor

//////////////////////////////////////////////////////////////////////////////////////////////////////

[GNS3 VPCS no path sorunu cozumu]

https://jono-moss.github.io/post/-gns3-install-debian-27-09-2024/

//////////////////////////////////////////////////////////////////////////////////////////////////////

[GNS3 UBRIDGE SORUNU COZUMU]

Debian 13'te uBridge paketi apt deposunda bulunmuyor, manuel derleme gerekiyor.Debian 13'te uBridge paketi depoda bulunmuyor, **kaynak koddan derlemen** gerekiyor. Bunun için önce gerekli bağımlılıkları kurman, sonra GitHub'dan derlemen gerekiyor.

Aşağıdaki komutları sırayla terminale yapıştır:

---

### Adım 1 — Gerekli araçları kur
```bash
sudo apt install git build-essential libpcap-dev -y
```

---

### Adım 2 — uBridge'i GitHub'dan çek ve derle
```bash
cd ~/Downloads
git clone https://github.com/GNS3/ubridge.git
cd ubridge
make
```

---

### Adım 3 — Sisteme kur
```bash
sudo make install
```

Bu komut uBridge'i `/usr/local/bin/ubridge` konumuna kurar.

---

### Adım 4 — Ağ yetkilerini ver
```bash
sudo setcap cap_net_admin,cap_net_raw=ep /usr/local/bin/ubridge
```

---

### Adım 5 — Kullanıcını gruplara ekle
```bash
sudo usermod -aG wireshark $(whoami)
```

---

### Adım 6 — Sistemi yeniden başlat
```bash
sudo reboot
```

---

### Adım 7 — Kurulumu doğrula
```bash
ubridge --version
```

Çıktı olarak `uBridge version 0.9.x` gibi bir şey görürsen kurulum başarılıdır. Ardından GNS3'ü aç, hata gitmiş olmalı.

Sorun devam ederse GNS3 içinde **Edit → Preferences → Server** kısmında uBridge yolunu `/usr/local/bin/ubridge` olarak manuel ayarla.

//////////////////////////////////////////////////////////////////////////////////////////////////////

[GNS3 uc cihazlara cift tiklama sonucu terminalin acilmamasi sorunu cozumu]

cihaza telnet yuklu degilse vpcs cihazlara gns3 telnet kullanarak baglandigindan cihaza telnet paketinin yuklu oldugundan emin olun ve acilacak terminal emulator uygulamasinin cihaz mevcut oldugundan emin olun aksi halde bunlari yukleyin.

//////////////////////////////////////////////////////////////////////////////////////////////////////

[GNS3 DOCKER ENTEGRASYONUNDA DOCKER.SOCK ILE ILGILI SORUNUN COZUMU]

docker.sock problemi yasaniyorsa `sudo usermod -aG docker $USER` bu komutu sistem de uygulayip sistemi yeniden baslatin muhtemelen sorun cozulecektir.

//////////////////////////////////////////////////////////////////////////////////////////////////////

[No available server support this type of node. You probably need to setup the GNS3 VM sorunu cozumu]

Bu hata GNS3'ün Docker'ı çalıştırmak için local server yerine GNS3 VM aradığı anlamına geliyor. 

GNS3'ü local server ile çalıştırmamız lazım. Şunu dene: GNS3'ü kapat, terminalde şunu çalıştır:

```bash
gns3server
```

Şimdi yeni bir terminal sekmesi aç ve GNS3 arayüzünü başlat:
bashgns3
Açıldığında Edit → Preferences → Server bölümüne git ve orada local server ayarlarını kontrol et.

//////////////////////////////////////////////////////////////////////////////////////////////////////

[No busybox executable could be found, please install busybox (apt install busybox-static on Debian/Ubuntu) and make sure it is in your PATH” Hatasi cozumu]

Bu hata genelde GNS3’ün çalıştığı sistemde busybox bulunamadığında çıkar — yani sorun çoğu zaman Docker image içinde değil, GNS3 Server’ın kurulu olduğu host makinede. 

GNS3’ü nerede çalıştırıyorsun?

🖥️ Lokal Linux makinede mi?
🖥️ Windows + GNS3 VM (VirtualBox/VMware) mi?
🖥️ Uzak GNS3 Server mı?

Çünkü çözüm ortama göre değişiyor.

Busybox'ı kur:

Debian / Ubuntu:
sudo apt update
sudo apt install busybox-static

Kurulduğunu doğrula:

which busybox

Eğer çıktı:

/usr/bin/busybox

şeklindeyse tamamdır.

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ NOTLAR ]

[GNS3 adapter terimi aciklamasi]

GNS3'te router cihazina verilen "adapter" sayisi o cihaza kac cihazin baglanabilecegini belirtir.
ornegin; "2 adapter" derken GNS3'ün o container'a kaç tane sanal ethernet portu vereceğini belirliyoruz
Şöyle düşün: Fiziksel bir router satın aldığında üzerinde kaç ethernet portu varsa o kadar cihaza bağlanabiliyorsun. GNS3'de adapter sayısı tam olarak bu — o sanal router'ın kaç ethernet portuna sahip olacağını belirliyor.
Yani 2 adapter = 2 ethernet portu = eth0 ve eth1 görüyorsun "ip a" da.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ip a komutunun ciktisinda gozuken ag arayuzlerinin anlamlari]

`ip a` (veya `ip addr`) komutu cihazın **ağ arayüzlerini** gösteriyor.

Şunu düşün: Fiziksel bir bilgisayarda ağ kartı var — ethernet portu, Wi-Fi kartı gibi. Bunların her biri bir ağ arayüzü.

`eth0`, `eth1` bunların sanal karşılıkları — her biri bir ethernet portu. Bağladığın her kablo bir `eth` arayüzüne denk geliyor.

`lo` ise **loopback** — fiziksel bir port değil, cihazın kendisiyle konuşması için özel bir sanal arayüz. `127.0.0.1` adresi hep buraya ait.

`enp...` gibi isimler ise daha yeni Linux sistemlerde kullanılan isimlendirme standardı — `eth0` yerine donanımın fiziksel konumuna göre isim veriliyor.


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[GNS3 Web arayuzunden ulasabilme yontemi]

GNS3 server'i bir vds, vpc veya uzak sunucuya kurup buna web arayuzunden erisebilme imkani mumkundur.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[GNS3 için ağ simulasyon programı deniliyor ancak içinde ki araçlar veya öğeler neden (routers, end devices vb.) yerleşik değil de entegre edilmelik?]

GNS3'ün tasarım felsefesi şu: "Ben sadece topolojiyi yöneteyim, cihazların içini sen doldur." Bunun avantajı esneklik — istediğin router yazılımını, istediğin işletim sistemini kullanabiliyorsun. Eğer GNS3 her şeyi içine gömseydi hem çok büyük olurdu hem de her yeni teknoloji için GNS3'ü güncellemen gererkirdi.

[ GNS3 server ile GNS3 GUI nedir neden ayrılar? ]

GNS3 server asıl işi yapan kısım — container'ları başlatıyor, bağlantıları kuruyor, trafiği yönetiyor. GUI ise sadece görsel arayüz. İkisi ayrı olduğundan GNS3 server uzak bir makinede de çalışabilir — sen kendi bilgisayarından GUI ile bağlanırsın.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ Proje pdf'inde ki kasıtlı olabileceğini düşündüğüm öğretici busybox kafa karıştırması ]

Proje de docker image'ler de "busybox" veya ona eşdeğer bir paketin mevcut bulunması isteniyor. Bu ayarlanıp ağ ayağa kaldırılmaya çalışıldığı zaman yukarı da "sorunlar" kısmında bahsi geçen "no path busybox.." hatası alınıyor GNS3 tarafından. Bu hata alındığında proje de docker image'ler de bulunulması istenilen "busybox" paketi ile ilgili bir anlığına sorun yaşanıldığı hissine kapanıldığı sanılabiliyor ancak sorunun bununla bir ilgisi olmadığı daha sonradan anlaşılıyor. Çünkü ana makine de gns3server docker konteynerlarını ayağa kaldırmadan evvel birkaç hazırlık yapması gerekiyor ve bunları belirli script'ler aracılığıyla sağlıyor. Bu script'lerde de busybox komutları kullanıldığından ana makinenin bu pakete sahip olması gerekiyor. Bu script'ler de busybox kullanılmasanının sebebi de gns3server'ın yapacağı hazırlıkların her farklı işletim sistemin de aynı şekilde çalışmasını sağlamak üzerine olduğundandır. Çünkü farklı linux işletim sistemlerinde temel linux komutları (ls, cp, mv vb.) farklı davranışlar sergileyebildiğinden gns3server'ın hazırlığı farklı sonuçlar verdirebilir. Bunun olmaması için her farklı makine de aynı davranışlar ile aynı hazırlıkların mümkün kılınabilmesi için busybox kullanılmaktadır. çünkü busybox komutları makineler farklı da olsa aynı davranışları sergileyecektir.

"init.sh" scripti şöyle başlıyor:
"#!/gns3/bin/busybox sh"

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ Peki ama docker konteynerlar ayaga kalktiktan sonra /gns3 klasörü ve scriptler neden var? ]

Bu scriptler GNS3 server ile container arasındaki köprü. kabaca düşünülcek olursa konteynerda yapılan değişikliklerin haberi gns3server'a iletilmesi gerekli ki gns3server'da bunu işlesin ve gns3 gui'da bunu yansıtsın. Bu yüzden bu script'ler konteyner'a mount ediliyor. ve temel olarak GNS3 server her container'ı başlatırken kendi init.sh scriptini container'a mount ediyor. Bu script şunları yapıyor:;

- Ağ arayüzlerini ayarlıyor (adapter sayisi verdigimiz)
- Telnet bağlantısını hazırlıyor (terminal ile makineyle iletisim kurabilmek icin)
- GNS3'ün container'ı yönetebilmesi için ortamı hazırlıyor

Kabaca genel yapı;
GNS3 GUI → GNS3 Server → init.sh (host busybox ile çalışır) → Container başlar → Telnet ile terminal açılır

Proje dokümanında docker image'lerine "busybox" kurdurması tamamen kafa karışıklığı yaratmak için ancak bu kafa karışıklığını yaratılmak istenmesinin sebebi kasıtlı. Bu kasıt gns3'un altyapısında "busybox" ın nasıl kullanıldığını öğretmek/anlatmak için. Container içerisine kurduğumuz busybox kullanılmıyor. /gns3 klasöründe ki bin klasörünün altında ki busybox kullanılıyor. muhtemelen bunu da ana makineden kopyalıyor.

Buna muteakip soyle bir trick ve optimizasyon yapilabilir; GNS3 zaten konteynerde ki /gns3 klasorune busybox'i kopyaladigindan oturu Docker image'e ekstradan bir daha busybox paketinin kurulmasina gerek yoktur.
Ancak buna uygun bir scirpt hazirlanmasi gerekli ki konteyner "/gns3/bin/busybox" dizininde ki busybox'i uygun sekilde calistirsin aksi taktirde nedeni bilinmeyen sekilde konteyner hemen exited durumuna dusuyor
. Script'in nasil hazirlanmasi gerektigine ipucu olarak proje dokumaninda part-1 bolumunde ki gorseller incelenebilir. Uygun script hazirlandigi taktirde proje dokumaninda ki busybox istegini karsilar nitelikte ve konteyner daha optimize olur.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ router yazilimi demek ne demek? router yazilimini bir makineye indirildiginde ne oluyor? ]

Şunu düşün: Fiziksel olarak bir router ile normal bir bilgisayar arasında aslında çok fark yok — ikisi de bir işlemci, RAM, ağ kartlarından oluşuyor. Fark şurada: **router yazılımı.**

Router yazılımı bir cihaza şu yetenekleri kazandırıyor:

```
Normal bilgisayar          Router yazılımı eklenince
─────────────────          ────────────────────────
Paket alır/gönderir   →    Paket alır, nereye göndereceğine karar verir
Tek ağa bağlı         →    Birden fazla ağ arasında köprü kurar
IP tablosu basit      →    Routing tablosu dinamik, OSPF/BGP ile güncellenir
```

Bizim topolojimizde de tam bunu yaptık — normal bir Linux container'a FRR kurarak ona router nitelikleri kazandırdık. O container artık:

- Birden fazla ağ arayüzüne sahip
- OSPF ile komşularını keşfedebiliyor
- Paketleri doğru yöne yönlendirebiliyor

Yani "router" aslında bir donanım değil, bir **rol** — ve bu rolü yazılım belirliyor. Bu yazilim makineye indirildiginde makine router nitelikli hale formlandirilabilir demek oluyor.

Cisco, Juniper gibi şirketlerin router'ları da özünde aynı şey — özel donanım üzerinde çalışan router yazılımları. FRR ise bu yazılımın açık kaynaklı versiyonu.


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[Gateway nedir?]

bir cihazdan `192.168.2.1`'e ping atmak istiyorsun. cihaz önce şunu soruyor: "Bu IP benim subnet'imde mi?"

`192.168.1.0/24` subnet'indeyim, hedef `192.168.2.1` — benim subnet'imde değil.

Bu durumda bir cihaz kendi subnet'i dışındaki bir hedefe paket göndermek istediğinde "ben bunu bilemem, bir üst cihaza sorayım" diyor. İşte o "üst cihaz" gateway.

Yani gateway = "bilmediğim her şeyi şuraya gönder" adresi.

bir VPCS cihazinda `ip 192.168.1.1/24 192.168.1.254` dediğinde:
- `192.168.1.1/24` → VPCS'nin kendi IP'si
- `192.168.1.254` → gateway, yani Router-1'in o taraftaki arayüzü

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[bir cihaza gateway atamasi yaparken "default" argumani ve onun haricinde gelebilecek argumanlarin anlami]

Gateway atamak için şu komutu kullaniliyor:

```
ip route add default via 192.168.1.254
```

`default` kelimesi "bilmediğin her şeyi şuraya gönder" demek. VPCS'deki gateway atamasıyla aynı mantık, sadece komut farklı.

veya ornegin soyle bir komut girdisi gelirse;

```
ip route add 192.168.2.0/24 via 192.168.1.254
```

Bu şunu söylüyor: "Sadece `192.168.2.0/24` subnet'ine gitmek istediğimde `192.168.1.254`'e gönder."

"default" ise bunun özel hali — "hiçbir rota eşleşmezse şuraya gönder" demek. Yani:

Spesifik rota  → sadece o subnet için geçerli
default        → hiçbir şey eşleşmezse buraya git

"default" netpractice'de ki router'da yapılan konfigürasyonlarda hatırlanabilir. network komutlarıyla (ip vb.) bu "default" daha iyi anlaşılmış oluyor.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ospf'in önemi ve o olmadan manuel yonlendirme ornegi]

belirli bir subnet'ten farklı bir subnet'e paket gönderimi yapılmak istendiğinde bunun için yönlendirme configuration'ı yapılması gerekir. şu şekilde bir topoloji örneği kurulduğunu tasavvur edelim;

VPCS-1 ── Router-1 ── Router-2 ── VPCS-2 (illa VPC olmak zorunda değil normal docker uç cihazları da olabilir)

bu ornekte 3 subnet (3 kablomuz) var (VPCS-1 --- [subnet 1] --- Router-1 --- [subnet 2] --- Router-2 --- [subnet 3] --- VPCS-2) ve su sekilde bir ağ arayuzu ayarlaması yapılabilir;

******************************************************
VPCS-1: 192.168.1.1/24
Router-1 eth0: 192.168.1.254/24  (VPCS-1 tarafı)
Router-1 eth1: 10.0.0.1/30       (Router'lar arası)
Router-2 eth0: 10.0.0.2/30       (Router'lar arası)
Router-2 eth1: 192.168.2.254/24  (VPCS-2 tarafı)
VPCS-2: 192.168.2.1/24
******************************************************

Ağ arayüzlerini bu şekilde ayarladıktan sonra VPCS-1'den VPCS-2 cihazına "ping 192.168.2.1" şeklinde ping atılmaya çalışıldığında başarız olunduğu görülebilir.

VPCS-1 cihazı "192.168.2.1" adresini 192.168.1.0 subnet'inde dogal olarak bulamadığından (farklı subnet'lere ait olmalarından) bu paketin üst bir cihaza yönlendirilmesi gerek. Bunun icin;

```
ip route add default via 192.168.1.254
```

aynı şekilde VPCS-2 cihazından da "192.168.1.1" adresine ping atılmak istenebilir bu yüzden benzer yönlendirme yapılandırılması yine şu şekilde yapılabilir;

```
ip route add default via 192.168.2.254
```

Özetle;
------------------------------------------------------
1. Router-1'de:
   eth0 → 192.168.1.254/24
   eth1 → 10.0.0.1/30

1. Router-2'de:
   eth0 → 10.0.0.2/30
   eth1 → 192.168.2.254/24

2. VPCS-1'de:
   IP: 192.168.1.1/24
   Gateway: 192.168.1.254

3. VPCS-2'de:
   IP: 192.168.2.1/24
   Gateway: 192.168.2.254
------------------------------------------------------

"ip route ip route add default via 192.168.1.254" komutuyla mevcut subnet'de adresi bulunamayan cihazın iletilmesi gereken paketlerini "192.168.1.254" IP adresine sahip cihaz aracılığıyla yönlendir diyoruz. Yine ping atmayı test edersek yine başarız olunduğu gözlemlenebilir. çünkü router-1 cihazı da aynı şekilde yönlendirme yapması gerekli çünkü ona gelen bu yabancı paketlerin nereye ve nasıl yönlendirilmesi gerektiği söylenmedi/yapılandırılmadı. router-1'de buna mukabil olarak bu yabancı paketleri ona komşu olan diğer router'a yani router-2'ye yönlendirmeli. Bu yüzden router-1 cihazinda bu komut uygulanabilir;

```
ip route add 192.168.2.0/24 via 10.0.0.2
```

kisacasi bu Bu "192.168.2.0/24'e gitmek istersen Router-2'den geç" diyor.

Ayrıca aynı yapılandırmayı router-2'de de yapmalıyız çünkü router-2'den de router-1'e bir geri dönüş "respond" paketleri gönderilecek. bu yüzden router-2'de benzer olarak;

```
ip route add 192.168.1.0/24 via 10.0.0.1
```

burada fark edilecegi uzere "default" kullanilmadi. Ancak kullanılabilirdi. Router-1'de "... default via 10.0.0.2" yazarsan "bilmediğin her şeyi Router-2'ye gönder" demiş olursun. Bu küçük topolojide işe yarar. Yani Router-1'de "default via Router-2" yazarsan tüm bilinmeyen trafiği Router-2'ye gönderiyorsun. Router-2 paketi doğru yere iletebilir. Ancak;

```
VPCS-1 ── Router-1 ── Router-2 ── Router-3 ── VPCS-2
                          └── Router-4 ── VPCS-3
```

şu şekilde bir topoloji düşünürsek ve Router-1'de "192.168.2.0/24 via Router-2" ve "192.168.3.0/24 via Router-2" gibi spesifik rotalar yazarsan tam olarak hangi trafiğin nereye gideceğini biliyorsun daha kontrollü.

Küçük ağlarda "default" pratik. Büyük ağlarda ise spesifik rotalar daha güvenilir.

bu mini tüyodan sonra "ping" komutu ile test yaparsak trafiğin başarılı olduğu gözlemlenebilir.

Ek olarak VPCS-1 cihazindan router-2'ye ping atılırsa; "ping 10.0.0.2" şeklinde neden ve nasıl paketler başarılı şekilde ulaşıyor?

VPCS-1 `10.0.0.2`'ye ping attığında şu oldu:

1. VPCS-1 "10.0.0.2 benim subnet'imde mi?" → Hayır → Gateway'ime göndereyim → Router-1'e gidiyor
2. Router-1 "10.0.0.2 nereye gider?" → Routing tablosuna bakıyor → `10.0.0.0/30` doğrudan bağlı, `eth1`'den çık → Router-2'ye ulaşıyor

Router-1'in zaten `10.0.0.0/30` subnet'ine doğrudan bağlı olması sayesinde mümkün. Az önce yapılandırması yapılan "ip route add 192.168.2.0/24 via 10.0.0.2, ip route add 192.168.1.0/24 via 10.0.0.1" mümkün kılınmadı. O iki komut ise şunun için gerekli: Router-1 `192.168.2.0/24`'ü bilmiyor, Router-2 `192.168.1.0/24`'ü bilmiyor. Bu komutlarla onlara "o subnet bu yönde" dedik.

ospfd servisin bize sağladığı şey ise bu yönlendirme yapılandırmasını otomatize etmek;

Şu an 2 router vardı ve 2 tane `ip route add` komutu yazdık — kolaydı. Ama şunu düşün:

100 router'lı bir ağda her router diğer 99 router'ın subnet'lerini bilmesi gerekiyor. Elle yazmak:
- Çok zaman alır
- Hata yapmak kolay
- Bir bağlantı kopsa veya yeni subnet eklenirse **her router'ı tek tek güncellemen** gerekir

OSPF bu işi otomatize ediyor:
- Yeni bir subnet eklendiğinde tüm router'lar otomatik öğreniyor
- Bir bağlantı kopunca routing tabloları otomatik güncelleniyor
- Sen hiçbir şeye dokunmak zorunda kalmıyorsun

Yani OSPF = manuel `ip route add` komutlarının otomatik ve dinamik versiyonu.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ ospfd servisinin onemini anlamaya yonelik yapilabilecek manuel yonlendirme topoloji egzersizleri/pratikleri/ornekleri ]


1. bu ornekte farkli subnet'lerde ki uc cihazlarin birbirlerine paket gonderirken router-1 cihazinda nasil spesifik olarak yonlendirilmesi gerektigi ayarlaniyor.
**************************
	VPCS-1
          |
        Router-1
       /        \
  Router-2    Router-3
     |              |
  VPCS-2         VPCS-3
**************************


2. Bu ornekte farkli subnet'e gidecek olan paketlerin hangi rotadan daha iyi gideceginin ayarlamalari manuel olarak yapiliyor veya baglanti kopma durumu oldugunda bu paketlerin alternatif hangi rotadan gitmesi gerektigi manuel olarak ayarlanmasi gerekiyor. 
(topolojiyi ve yonlendirme yapilandirmalari yapildiktan sonra her bir uc cihazin diger uc cihazlara erisimini ping ile test edin. hepsi birbirlerine duzgun sekilde ping gonderebiliyorlarsa router-1 ile router-2'nin baglantisini kesin ve tekrardan birbirlerine ping atmayi deneyin. basarisiz olursaniz bunu cozmeyi deneyin.)
********************************************
VPCS-1 ── Router-1 ── Router-2 ── VPCS-2
              |              |
           Router-3 ── Router-4
              |
           VPCS-3
********************************************

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ ospf'e router'ların network adreslerini tanıtırken kullanılan "area 0" ın anlamı nedir? ]

Çok büyük bir ağda yüzlerce router var. Hepsi birbirine OSPF ile bağlıysa her router tüm ağın haritasını tutmak zorunda — bu çok ağır olur.
Area sistemi ağı **bölgelere** ayırıyor:

```
Area 0 (backbone)
    ├── Area 1
    ├── Area 2
    └── Area 3
```

Her area kendi içinde OSPF çalıştırıyor. Area'lar arası geçiş için **Area 0** merkez görevi görüyor — tüm diğer area'lar mutlaka Area 0'a bağlanmak zorunda.
Peki `area 1` veya `area 2` yapsak ne değişir? Eğer bazı router'lar `area 0`, bazıları `area 1` derse — bu iki group birbirini göremez, aralarında özel bir **ABR (Area Border Router)** gerekir.
Bizim küçük topolojimizde tek area yeterli — hepsi `area 0`. Büyük ağlarda ise performans için birden fazla area kullanılır.

OSPF'de her router komşularından "ben şu subnet'lere sahibim" bilgisini alıyor. Bu bilgiler birikince router'ın aklında tüm ağın haritası oluşuyor.

Örneğin 100 router'lı bir ağda:
- Router-1, Router-2'den öğreniyor
- Router-2, Router-3'ten öğreniyor
- Bu zincir devam ediyor
- Sonunda Router-1 tüm 100 router'ın subnet bilgisine sahip

Buna **LSDB (Link State Database)** deniyor — her router'ın aklındaki ağ haritası.
100 router küçük bir ağ için sorun değil. Ama 10.000 router'lı bir ağda her router 10.000 router'ın bilgisini tutmak zorunda kalırsa — bu çok fazla bellek ve işlemci gücü demek.
Area sistemi bunu çözüyor: Router-1 sadece kendi area'sının haritasını tutuyor, tüm ağın değil.

[ (once ki soruya ek olarak) ama router tüm ağın haritasını tutması gerekli değil mi? sonucta en kisa rotayi veya baglanti sorunu oldugu zaman alternatif rota ayarlamasi yapmasi gerekli ]

router'ın en kısa yolu bulması için haritaya ihtiyacı var.
Ama: 10.000 router'lı dev bir ağda Router-1'in Japonya'daki bir router'ın detaylı haritasını bilmesi gerekiyor mu? Yoksa "Japonya'ya gitmek istersen şu yönden git" bilgisi yeterli mi?
Area sistemi tam bunu yapıyor:

```
Area 1 (Türkiye)    Area 2 (Japonya)
    Router-1  ────────── ABR ────────── Router-500
```
Router-1 kendi area'sının detaylı haritasını biliyor. Japonya tarafı için sadece "ABR'den geç" biliyor — Japonya'nın iç detaylarını bilmesi gerekmiyor.
Yani her şeyi bilmek yerine **yeterince** bilmek — bu area sisteminin özü.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ ospf area egzersizi ]

```
VPCS-1 ── Router-1 ── Router-2 ── Router-3 ── VPCS-2
```

Bu topoloji kurulup IP planlamasi yapildiktan sonra ospf'de su sekilde ABR ayari yapilabilir;

Router-1 ve Router-2 → Area 0
Router-2 ve Router-3 → Area 1

Bunun icin;

Router-1;

```
vtysh
configure terminal
router ospf
network 192.168.1.0/24 area 0
network 10.0.0.0/30 area 0
exit
exit
write
```

Router-2 (ABR olan cihaz);

```
vtysh
configure terminal
router ospf
network 10.0.0.0/30 area 0
network 10.0.0.4/30 area 1
exit
exit
write
```

Router-3;

```
vtysh
configure terminal
router ospf
network 10.0.0.4/30 area 1
network 192.168.2.0/24 area 1
exit
exit
write
```

Yapilandirmalar yapildiktan sonra uc cihazlara ping gonderimini deneyin ardindan router-1 ve router-3 cihazlarinin kac tane router kaydi oldugunu gormek icin router yazilimindayken (vtysh'dayken);

```
show ip ospf database
```
veya
```
show ip ospf database router
```

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ wireshark'i gns3 ile kullanma ve buna mutekakiben ag trafigini izleme ]

Herhangi bir topolojide ki ag trafiğini izleyebilmek için ana makineye "wireshark" kurulmalıdır (Kurulum sırasında "non-root users can capture packets" sorusu çıkacak — Yes de); 

```
sudo apt install wireshark
```

Kurulum tamamlandiktan sonra GNS3'de ki bir topolojide iki cihaz arasinda ki kabloya sag tikla ve "start capture" secenegine tikla. Bununla beraber Wireshark acilacak. Açıldıktan sonra bir router'ın terminalinde ping at veya OSPF çalışıyorsa zaten paketler görünmeye başlayacak.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

[ Wireshark "Couldn't run dumpcap in child process: Permission denied" hatasi ]

izin sorununu cozmek icin;

```
sudo usermod -aG wireshark $USER
```

ve ana makineye restart at.

###############################################################
#                                                             #
#                                                             #
#    ____       _      ____    _____                 ____     #
#   |  _ \     / \    |  _ \  |_   _|               |___ \    #
#   | |_) |   / _ \   | |_) |   | |      _____        __) |   #
#   |  __/   / ___ \  |  _ <    | |     |_____|      / __/    #
#   |_|     /_/   \_\ |_| \_\   |_|                 |_____|   #
#                                                             #
#                                                             #
###############################################################

