## Konu Başlıkları
  - [GNS3 Kurulum Sorunları ve Çözümleri](#gns3-kurulum-sorunları-ve-çözümleri)
    - [`dynamips` ve `software-properties-common` paketleri sorunu](#dynamips-ve-software-properties-common-paketleri-sorunu)
    - [`No busybox executable could be found, please install busybox (apt install busybox-static on Debian/Ubuntu) and make sure it is in your PATH` hatası](#no-busybox-executable-could-be-found-please-install-busybox-apt-install-busybox-static-on-debianubuntu-and-make-sure-it-is-in-your-path-hatası)
    - [VPCS ağ cihazları ile ilgili hatalar](#vpcs-ağ-cihazları-ile-ilgili-hatalar)
      - [`No path to a VPCS executable has been set` hatası](#no-path-to-a-vpcs-executable-has-been-set-hatası)
      - [`VPCS executable version must be >= 0.6.1 but not a 0.8` hatası](#vpcs-executable-version-must-be--061-but-not-a-08-hatası)
    - [GNS3 `uBridge not avaiable` hatası](#gns3-ubridge-not-avaiable-hatası)
    - [GNS3 SIP Module ve QT sorunu](#gns3-sip-module-ve-qt-sorunu)
    - [Topolojide ki cihazların terminallerinin açılmaması](#topolojide-ki-cihazların-terminallerinin-açılmaması)
  - [Docker Entegrasyonu](#docker-entegrasyonu)
    - [docker.sock ile ilgili sorunun çözümü](#dockersock-ile-ilgili-sorunun-çözümü)
    - [Docker image'lerini GNS3'e entegre etme](#docker-imagelerini-gns3e-entegre-etme)
    - [`No available server support this type of node. You probably need to setup the GNS3 VM` sorunu çözümü](#no-available-server-support-this-type-of-node-you-probably-need-to-setup-the-gns3-vm-sorunu-çözümü)
  - [GNS3 Temelleri](#gns3-temelleri)
    - [GNS3'te "adapter" ne demek?](#gns3te-adapter-ne-demek)
    - [GNS3 Web Client ile Web üzerinden GNS3 çalıştırmak](#gns3-web-client-ile-web-üzerinden-gns3-çalıştırmak)
    - [GNS3'ün modüler bir yazılım olması üzerine](#gns3ün-modüler-bir-yazılım-olması-üzerine)
    - [Proje dokümanında öğreticilik açısından kasıtlı olarak yapıldığını düşündüğüm busybox kafa karıştırması](#proje-dokümanında-öğreticilik-açısından-kasıtlı-olarak-yapıldığını-düşündüğüm-busybox-kafa-karıştırması)
    - [Docker konteynerlar çalıştıktan sonra içlerinde barındırılan `/gns3` klasörü ve script'leri](#docker-konteynerlar-çalıştıktan-sonra-içlerinde-barındırılan-gns3-klasörü-ve-scriptleri)
  - [Temel Ağ Kavramları](#temel-ağ-kavramları)
    - [`ip a` komutunun çıktısında gözüken ağ arayüzlerinin anlamları](#ip-a-komutunun-çıktısında-gözüken-ağ-arayüzlerinin-anlamları)
    - [Data, Segment, Frame ve Bit nedir ve ne içerir?](data-segment-frame-ve-bit-nedir-ve-ne-içerir)
    - [Router yazılımı ne demek? Router yazılımı bir cihaza indirildiğinde ne oluyor?](#router-yazılımı-ne-demek-router-yazılımı-bir-cihaza-indirildiğinde-ne-oluyor)
    - [FRR yazilim çatısı altında ki diğer yazılımların işlevleri](#frr-yazilim-çatısı-altında-ki-diğer-yazılımların-işlevleri)
    - [Gateway Nedir?](#gateway-nedir)
    - [Aynı subnet içinde ki uç cihaza gönderilen bir paketin yolculuğu](#aynı-subnet-içinde-ki-uç-cihaza-gönderilen-bir-paketin-yolculuğu)
    - [Farklı subnet'te ki uç cihaza gönderilen bir paketin yolculuğu](#farklı-subnette-ki-uç-cihaza-gönderilen-bir-paketin-yolculuğu)
    - [Bir uç cihaza gateway ataması yaparken `default` argümanı ve onun haricinde gelebilecek argümanların anlamı](#bir-uç-cihaza-gateway-ataması-yaparken-default-argümanı-ve-onun-haricinde-gelebilecek-argümanların-anlamı)
    - [Manuel yönlendirme örneği ve buna müteakip OSPF'in öneminin anlaşılması](#manuel-yönlendirme-örneği-ve-buna-müteakip-ospfin-öneminin-anlaşılması)
    - [OSPF'in önemini anlamaya yönelik yapılabilecek manuel yönlendirme topoloji egzersizleri/pratikleri/örnekleri](#ospfin-önemini-anlamaya-yönelik-yapılabilecek-manuel-yönlendirme-topoloji-egzersizleripratikleriörnekleri)
    - [OSPF'e router'ların network adreslerini tanıtırken kullanılan `area 0`'ın anlamı nedir?](#ospfe-routerların-network-adreslerini-tanıtırken-kullanılan-area-0ın-anlamı-nedir)
      - [Ama router tüm ağın haritasını tutması gerekli değil mi? Sonuçta en kısa rotayı veya bağlantı sorunu oldugu zaman alternatif rota ayarlaması yapması gerekli](#ama-router-tüm-ağın-haritasını-tutması-gerekli-değil-mi-sonuçta-en-kısa-rotayı-veya-bağlantı-sorunu-oldugu-zaman-alternatif-rota-ayarlaması-yapması-gerekli)
    - [OSPF `area` egzersizi](#ospf-area-egzersizi)
  - [Wireshark GNS3 Entegrasyonu](#wireshark-gns3-entegrasyonu)
    - [Wireshark'ı GNS3 ile kullanma ve buna mütekakiben ağ trafiğini izleme](#wiresharkı-gns3-ile-kullanma-ve-buna-mütekakiben-ağ-trafiğini-izleme)
    - [Wireshark `Couldn't run dumpcap in child process: Permission denied` hatası](#wireshark-couldnt-run-dumpcap-in-child-process-permission-denied-hatası)


## Part 1

### GNS3 Kurulum Sorunları ve Çözümleri
Proje dokümanında projenin bir sanal makine üzerinde yapılması isteniliyor. GNS3 ve bağımlılık paketleri mevcut sisteminizi gereksiz yere şişirip kirletebileceğinden tüm işlemleri bir sanal makine de yapmak da en iyisi olacaktır. Tüm işlemler **Debian 13** üzerinden yürütülmüştür. Bu yüzden GNS3 kurulumu esnasında yaşanan sorunların bir kısmı Debian 13 ile ilgilidir.

#### `dynamips` ve `software-properties-common` paketleri sorunu
GNS3'ün resmi web sitesinden Debian ve Debian tabanlı dağıtımlar için GNS3 ve gerekli olan bağımlılık paketlerini yüklemeye çalışırken bağımlılık hatası alınır. Debian 13 ve Debian 13 tabanlı dağıtımlarda, `dynamips` ve `software-properties-common` paketleri `apt` deposundan kaldırılmıştır; bu nedenle, `dynamips` olmadan yükleme yapıp ardından `dynamips`'i ayrı olarak yükleyeceğiz. Önce resmi web sitesinde ki yükleme adımlarında ki komut satırından `dynamips` ve `software-properties-common` paketlerini kaldırıp GNS3 için gerekli paketleri sisteme yükleyin;

```sh
sudo apt install python3 python3-pip pipx python3-pyqt6 python3-pyqt6.qtwebsockets python3-pyqt6.qtsvg qemu-kvm qemu-utils libvirt-clients libvirt-daemon-system virtinst ca-certificates curl gnupg2 
```

Şimdi `dynmaips` paketini ayrı olarak sisteme yükleyin;

```sh
wget http://ftp.us.debian.org/debian/pool/non-free/d/dynamips/dynamips_0.2.14-1_amd64.deb
```

ardından;

```sh
sudo dpkg -i dynamips_0.2.14-1_amd64.deb
```

Bunun ardından resmi web sitesinde ki `pipx` ile GNS3 server ve GUI'ı kurma adımından devam edebilirsiniz.

#### `No busybox executable could be found, please install busybox (apt install busybox-static on Debian/Ubuntu) and make sure it is in your PATH` hatası

Bu hata genelde GNS3’ün çalıştığı sistemde busybox bulunamadığında çıkar — yani sorun çoğu zaman Docker image içinde değil, GNS3 Server’ın kurulu olduğu ana makinede.

Busybox'ı kur:

```sh
sudo apt update
sudo apt install busybox-static
```

Kurulduğunu doğrula:

```sh
which busybox
```

Eğer çıktı:

```sh
/usr/bin/busybox
```

şeklindeyse busybox indirilmiştir.

#### VPCS ağ cihazları ile ilgili hatalar
##### `No path to a VPCS executable has been set` hatası
VPCS cihazlarını topolojinizde kullanmaya çalıştığınızda bu hata GNS3 tarafından verilebilir. Bunun sebebi ana sisteme `vpcs` paketinin kurulu olmamasından kaynaklıdır;

```sh
sudo apt install vpcs
```

##### `VPCS executable version must be >= 0.6.1 but not a 0.8` hatası
`vpcs` paketini sisteme kurup tekrardan topolojiyi ayağa kaldırmaya çalıştığınızda bu seferde bir _**version missmatch**_ hatası alabilirsiniz. Bunu çözmek için versiyonu yüksek olan `vpcs` paketini kaynak koddan derleyip sisteme yüklemek gereklidir bunun için;

```sh
wget https://github.com/GNS3/vpcs/archive/refs/tags/v0.8.3.zip
```

indirdikten sonra, `.zip` dosyasını açın ve içinde ki `src` klasörüne gidin;

```sh
cd v0.8.3/src
```

ardından VPCS scrpit'ini çalıştırmak için aşağıdaki komutu çalıştırın bu kaynak dosyaları derleyecektir;

```sh
./mk.sh
```

derleme işlemi tamamlandığında, VPCS'nin eski sürümünü kaldırın;

```sh
sudo rm /usr/bin/vpcs
```

Ardından yeni versiyonu `/usr/bin/` dizinine kopyalayın. Örneğin:

```sh
sudo cp /home/$USER/v0.8.3/src/vpcs /usr/bin/vpcs
```

#### GNS3 `uBridge not avaiable` hatası

Debian 13'te uBridge paketi depoda bulunmadığından, **kaynak koddan derleme** gerekiyor. Bunun için önce gerekli bağımlılıkları kurman, sonra GitHub'dan paketi indirip derlemen gerekiyor;

Öncelikle gerekli bağımlılıkları sisteme kuruyoruz;

```sh
sudo apt install git build-essential libpcap-dev -y
```

ardından uBridge'i Github'dan çekip ve derleyelim;

```sh
git clone https://github.com/GNS3/ubridge.git
cd ubridge
make
```

derleme tamamlandıktan sonra sisteme uBridge'i kurabiliriz;

```sh
sudo make install
```

uBridge `/usr/local/bin/ubridge` dizinine kurulacaktır.

Ardından uBridge'e ağ yetkilerini verelim;

```sh
sudo setcap cap_net_admin,cap_net_raw=ep /usr/local/bin/ubridge
```

kullanıcını gruplara ekleyelim;

```sh
sudo usermod -aG wireshark $(whoami)
```

Sistemi yeniden başlatalım;

```sh
sudo reboot
```

Kurulumu doğrulayalım;

```sh
ubridge --version
```

Çıktı olarak `uBridge version 0.9.x` gibi bir şey görürsek kurulum başarılıdır. Ardından GNS3'ü açtığımızda hata gitmiş olmalı. Sorun devam ederse GNS3 içinde `Edit → Preferences → Server` kısmında uBridge yolunu `/usr/local/bin/ubridge` olarak manuel ayarlayalım.

#### GNS3 SIP Module ve QT sorunu
`pipx` ile kurulan GNS3, eksik sistem kütüphaneleri nedeniyle başlamayabilir;
- GNS3'ün yeni sürümleri PyQt5 değil **PyQt6** gerektiriyor
- `pipx` izole ortam oluşturduğu için PyQt6'yı manuel inject etmek gerekiyor
- Debian 13 minimal kurulumda PyQt6'nın ihtiyaç duyduğu **XCB kütüphaneleri** varsayılan olarak gelmiyor

Çözüm için;

1. **PyQt6'yı pipx ortamına inject edelim:**

```bash
pipx inject gns3-gui PyQt6
```

2. **Eksik XCB sistem kütüphanelerini kuralım:**

```bash
sudo apt install libxcb-cursor0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0
```

3. **GNS3'ü başlatalım:**

```bash
gns3
```

#### Topolojide ki cihazların terminallerinin açılmaması
Topolojide ki cihazlara çift tıklandıldığında veya sağ tıklayıp `Console` seçeneğine basıldığında şayet o ağ cihazının terminal ortamı açılmıyorsa ana sistem de `telnet` paketinin yükü olduğundan emin olun. GNS3 kurduğunuz topolojilerde ki ağ cihazlarının terminal ortamlarına `telnet` kullanarak bağlandığından ana sistem de bunun yüklü olması gereklidir. Ayrıca `telnet` ile bağlantı kurulduktan sonra açılacak olan terminal emülator uygulamasının da ana sistem de mevcut olduğunu doğrulayın. Terminal emülator uygulaması GNS3'de `Edit -> Preferences -> General -> Console applications -> Console Settings` bölümünden `Edit` diyerek sistem de mevcut olan terminal emülatorü seçilebilir veya değiştirilebilir.

### Docker Entegrasyonu

#### docker.sock ile ilgili sorunun çözümü
**docker.sock** problemi yaşanıyorsa `sudo usermod -aG docker $USER` bu komutu ana sistem de uygulayıp sistemi yeniden başlatın sorun çözülmüş olacaktır.

#### Docker image'lerini GNS3'e entegre etme
Ana sisteme docker yükleyip custom docker image'leri hazır hale getirdikten sonra GNS3'de bu imajları kullanabilmek için GNS3'de `Edit -> Preferences -> Docker -> Docker Containers -> New -> Existing Image` diyerek listeden docker image'lerinizi seçerek GNS3'e ekleyebilirsiniz.

#### `No available server support this type of node. You probably need to setup the GNS3 VM` sorunu çözümü

Bu hata GNS3'ün Docker'ı çalıştırmak için local server yerine GNS3 VM aradığı anlamına geliyor. GNS3'ü local server ile çalıştırmamız lazım. Şunu dene: GNS3'ü kapat, terminalde şunu çalıştır:

```bash
gns3server
```

Şimdi yeni bir terminal sekmesi aç ve GNS3 GUI'ı başlat:

```bash
gns3
```

Açıldığında `Edit → Preferences → Server` bölümüne git ve orada **local server** ayarlarını kontrol et.
### GNS3 Temelleri

#### GNS3'te "adapter" ne demek?
GNS3'te router cihazina verilen **adapter** sayısı o cihaza kaç cihazın bağlanılabileceğini belirtir. Örneğin **_2 adapter_** dediğiniz takdirde; `ip a` komutunu ilgili makine üzerinde çalıştırırsanız çıktı olarak **eth0 ve eth1** sanal internet arayüzlerini görürsünüz.

#### GNS3 Web Client ile Web üzerinden GNS3 çalıştırmak
GNS3 yazılımı iki parçadan oluşuyor; GNS3 GUI (client kısmı) ve GNS3 server kısmı.
GNS3 server asıl işi yapan kısım. Container'ları başlatıyor, bağlantıları kuruyor, trafiği yönetiyor. GUI ise sadece görsel arayüz. İkisi ayrı olduğundan GNS3 server uzak bir makinede de çalışabilir. Herhangi bir PC'de ki GNS3 GUI (cilent) ile bağlanırsın ve bu ayrım sayesinde GNS3'ün server kısmını uzak bir sunucuya kurup bunu dışarıdan erişilebilir hale getirdikten sonra herhangi bir GNS3 client'ından bu server'a bağlanarak GNS3 çalıştırılabilir hale getirebilirsin. Ortak çalışmalar için kullanışlı bir çözüm olabilir.

#### GNS3'ün modüler bir yazılım olması üzerine
GNS3 bir simülasyon programı ise router, end devices vb. ağ cihazlarını ve öğelerini hazır olarak barındırması gerekmez mi? Neden bazı ağ cihazları mevcut iken (ethernet switch, VPCs vb.) bazı ağ cihazları (routers vb.) GNS3 içerisinde hazır olarak mevcut değil? Tarzında soru sorulabilir. Bunun cevabı GNS3'ün tasarım biçimindedir. GNS3'ün tasarım hedefi şu: "Ben sadece topolojiyi yöneteyim, cihazları sen oluştur ve içini sen doldur." Bunun avantajı esneklik — istediğin router yazılımını, istediğin işletim sistemini kullanabiliyorsun. Eğer GNS3 her şeyi içine gömseydi hem çok büyük olurdu hem de her yeni teknoloji için GNS3'ü güncellemen gerekirdi. İşte bu sayede GNS3'ün Docker ile entegrasyonuyla istenilen imajlar ile istenilen ağ cihazı oluşturulabilir ve bu GNS3'e entegre edilip ağ topolojilerinde kullanılabilir hale getirilebilir. Docker'ın yanı sıra VPCS gibi PC simulasyon araçlarının kullanılabilmesinin sebebi tamamen GNS3'e entegre edilmesidir. Yani ana makinenize `vpcs` paketini yüklemediyseniz GNS3'te bu mini PC simülatörlerinin kullanımı mümkün değildir. Bunlar GNS3'e has gömülü ağ cihazları değildir. Tıpkı Docker'da olduğu gibi entegre edilmesi gereken araçlardır. 

#### Proje dokümanında öğreticilik açısından kasıtlı olarak yapıldığını düşündüğüm busybox kafa karıştırması
Proje dokümanında docker image'ler de **busybox** veya ona eşdeğer bir paketin mevcut bulunması istendiği belirtiliyor. Bu ayarlanıp bir topoloji ayağa kaldırılmaya çalışıldığı zaman GNS3 `no path busybox..` hatası veriyor. Bu hata alındığında proje de docker image'ler de bulunulması istenilen **busybox** paketi ile ilgili bir anlığına sorun yaşanıldığı sanılabiliyor. Ancak sorunun bununla bir ilgisi olmadığının bilinmesi gerek. Çünkü ana makine de `gns3server` docker konteynerlarını ayağa kaldırmadan evvel birkaç hazırlık yapması gerekiyor ve bunları belirli script'ler aracılığıyla sağlıyor. Bu script'lerde de busybox komutları kullanıldığından aslında ana makinenin `busybox` paketine sahip olması gereklidir. Sorunun docker image'lerde yüklenmeye çalışılan busybox paketiyle bir ilgisi yoktur. Bu yanılgıya düşülmemelidir. GNS3'ün bu script'ler de busybox kullanmasının sebebi de `gns3server`'ın yapacağı hazırlıkların her farklı işletim sistemin de aynı şekilde çalışmasını sağlamak üzerine olduğundandır. Çünkü farklı Linux işletim sistemlerinde temel Linux komutları (ls, cp, mv vb.) farklı davranışlar sergileyebildiğinden `gns3server`'ın hazırlığı farklı sonuçlar verebilir. Bunun olmaması için her farklı makine de aynı davranışlar ile aynı hazırlıkların mümkün kılınabilmesi için busybox kullanılmaktadır. Çünkü busybox komutlarının tipik davranışı olarak işletim sistemi farklı da olsa aynı davranışları sergileyecektir.

GNS3'ün hazırlık script'lerinden `init.sh` script'i nasıl başladığını bakmak isteyebilirsiniz:
```sh
#!/gns3/bin/busybox sh
```

#### Docker konteynerlar çalıştıktan sonra içlerinde barındırılan `/gns3` klasörü ve script'leri
Docker imajları ile oluşturulmuş ağ cihazlarının GNS3'de ki bir topoloji de kullanılıp bu topoloji ayağa kaldırıldıktan sonra bu ağ cihazlarının terminal ortamına girildiğinde `/gns3` ve bu klasörün içerisinde yine GNS3 hazırlık script'leri görülebilir. Bu klasör ve script'lerin neden halen içlerinde barındırıldığına dair bir soru yöneltilecek olursa; Bu scriptler GNS3 server ile container arasındaki köprü olmasındandır. Kabaca düşünülecek olursa konteynerda yapılan değişikliklerin (ip adresi atama ve diğer benzeri konfigürasyonlar) haberi `gns3server`'a iletilmesi gerekli ki `gns3server`'da bunu işlesin ve GNS GUI'da bunu yansıtsın. Bu yüzden bu script'ler konteyner'a mount ediliyor. Ve temel olarak GNS3 server her container'ı başlatırken kendi `init.sh` scriptini container'a mount ediyor. Bu script şunları yapıyor;

- Ağ arayüzlerini ayarlıyor (örneğin kaç adet adapter sayısı verdiysek o kadar arayüz oluşturma)
- Telnet bağlantısını hazırlıyor (terminal ile makineyle iletişim kurabilmek için)
- GNS3'ün container'ı yönetebilmesi için ortamı hazırlıyor

Kabaca genel yapı;
```
GNS3 GUI → GNS3 Server → init.sh (host busybox ile çalışır) → Container başlar → Telnet ile terminal açılır
```

Script'ler için `/gns3` klasöründe ki `bin` klasörünün altında ki `busybox` kullanılıyor. Bunu da ana makineden kopyalıyor. Ayrıca madem `/gns3` klasörü docker konteynerına kopyalanıyor ve bununla beraber ana makinede ki `busybox` aracıda kopyalanmış oluyor o zaman buna müteakip şöyle bir trick ve optimizasyon yapilabilir; GNS3 zaten konteynerde ki `/gns3` klasörüne busybox'i kopyaladığından ötürü Docker image'e ekstradan bir daha busybox paketinin kurulmasına gerek yoktur. Ancak buna uygun bir Dockerfile veya Dockerfile'ın çalıştıracağı bir script hazırlanması gerekli ki konteyner `/gns3/bin/busybox` dizininde ki busybox'i uygun şekilde çalıştırabilsin aksi taktirde nedeni bilinmeyen şekilde konteyner hemen `exited` durumuna düşüyor. Script'in nasıl hazırlanması gerektiğine ipucu olarak proje dokümaninda Part 1 bölümünde ki görseller incelenebilir. Uygun script hazırlandığı taktirde proje dokümanında ki busybox isteğini karşılar nitelikte olur ve konteyner daha optimize olur.

### Temel Ağ Kavramları
#### `ip a` komutunun çıktısında gözüken ağ arayüzlerinin anlamları
`ip a` (veya `ip addr`) komutu mevcut cihazın **ağ arayüzlerini** gösteriyor. Şöyle ki: Fiziksel bir bilgisayarda ağ kartı var — ethernet portu, Wi-Fi kartı gibi. Bunların her biri bir ağ arayüzü. `eth0`, `eth1` bunların sanal karşılıkları/temsilleri — her biri bir ethernet portu. Bağladığın her kablo bir `eth` arayüzüne denk geliyor. `lo` ise **loopback** — fiziksel bir port değil, cihazın kendisiyle konuşması için özel bir sanal arayüz. `127.0.0.1` adresi hep buraya ait. `enp` öneki ile başlayan isimler ise daha yeni Linux sistemlerde kullanılan isimlendirme standardı — `eth0` yerine donanımın fiziksel konumuna göre isim veriliyor.

### Data, Segment, Frame ve Bit nedir ve ne içerir?
**Data (Layer 5 - 7)**: TCP/IP'deki uygulama katmanı, OSI'deki layer 5 - 6 ve 7'yi kapsar. Kullanıcının doğrudan etkileşime girdiği ham içeriktir. İçeriği örnek olarak bir web sayfasının HTML kodları, bir e-posta metni, bir görsel veya MP3 dosyası olabilir.
**Segments (Layer 4)**: Ham ve tüm verinin internette daha rahat taşınabilmesi için daha küçük parçalara bölünmüş halidir (üst katmandan gelen verinin). İçeriği Port numarası, Sequence Numbers (TCP'de paketlerin karşı tarafta doğru sırayla birleştirilmesini sağlamak için), Checksum (Verinin taşıma esnasında bozulup bozulmadığını denetlemek için.) bulunur.
**Packets (Layer 3)**: Segmentlerin üzerine IP'lerin eklendiği katmandır. Verinin hangi ip'den hangi IP'ye gideceği ve TTL bilgilerini içerir.
**Frames (Layer 2)**: MAC adreslerinin yazıldığı katmandır.
**Bits (Layer1)**: Fiziksel ortamda bilginin karşı tarafa iletilebilmesi için 0 ve 1'lere ayrıştığı halidir.

#### Router yazılımı ne demek? Router yazılımı bir cihaza indirildiğinde ne oluyor?
Fiziksel olarak bir router ile normal bir bilgisayar arasında aslında çok fark yok — ikisi de bir işlemci, RAM, ağ kartlarından oluşuyor. Fark şurada: 

Router yazılımı bir cihaza şu yetenekleri kazandırıyor:

```
Normal bilgisayar          Router yazılımı eklenince
─────────────────          ────────────────────────
Paket alır/gönderir   →    Paket alır, nereye göndereceğine karar verir
Tek ağa bağlı         →    Birden fazla ağ arasında köprü kurar
IP tablosu basit      →    Routing tablosu dinamik, OSPF/BGP ile güncellenir
```

Biz de tam bunu yaptık — Docker konteynera FRR kurarak ona router nitelikleri kazandırdık. O container artık:

- Birden fazla ağ arayüzüne sahip
- OSPF ile komşularını keşfedebiliyor (konfigüre edildiği taktirde)
- Paketleri doğru yöne yönlendirebiliyor

Yani "router" aslında bir donanım değil, bir **rol** — ve bu rolü yazılım makineye veriyor. Bir Laptop, mobil cihaz üzerine router yazılımı kurulabiliyorsa bu cihazlarda router cihazı gibi davrandırılabilir. Cisco, Juniper gibi şirketlerin router'ları da özünde aynı şey — özel donanım üzerinde çalışan router yazılımları. FRR ise bu yazılımın açık kaynaklı versiyonu.

#### FRR yazilim çatısı altında ki diğer yazılımların işlevleri
Zebra ve Quaagga FRR'nin koordinatörleri ancak aktif olarak FRR'da **zebra** kullanıldığından zebra routing tablosunu yönetiyor. Diğer tüm servisler (ospfd, bgpd, isisd) öğrendikleri rota bilgilerini zebra'ya bildiriyor, zebra bunları Linux kernel'in routing tablosuna yazıyor. Zebra olmadan diğer servisler kernel ile konuşamıyor. Manuel olarak `ip route 192.168.1.0/24 10.0.0.1` yazıldığında, işletim sistemi çekirdeğine (Kernel) doğrudan emir verirsin. Tek tek `ip route` yazmak yerine; Zebra, protokollerden gelen dinamik bilgileri kullanarak o `ip route` komutlarını saniyeler içinde ve sürekli güncelleyerek otomatik olarak takip eder ve arka planda çalıştırır. Zebra bu durumu otomatik hale getirir;

- Haber Toplama: BGP veya OSPF gibi protokoller, komşu cihazlardan _"Şu ağ bende var!"_ bilgisini alır.
- Karar Verme: Zebra bu bilgileri   toplar. Eğer aynı yere giden iki yol varsa, en iyisini seçer.
- Uygulama: Zebra, seçtiği en iyi rotayı senin yerine otomatik olarak işletim sisteminin yönlendirme tablosuna (Kernel/FIB) yazar.

**Quagga** ise FRR'nin eski hali. Artık aktif olarak geliştirilmiyor. FRR, Quagga'dan fork edildi ve devam etti. Proje dökümanında _"zebra veya quagga"_'dan bahsediyor çünkü ikisi de aynı işi yapıyor, sadece biri eski diğeri yeni.

**IS-IS** ve isisd ise IS-IS = Intermediate System to Intermediate System. OSPF gibi bir iç routing protokolü. Aynı AS (autonomous system) içinde router'ların birbirini keşfetmesi için kullanılıyor. IS-IS büyük telekom ağlarında tercih ediliyor daha ölçeklenebilir ve IP'den bağımsız çalışıyor. OSPF ise kurumsal ağlarda daha yaygın. OSPF daha çok kurumsal ağlarda (ofisler, kampüsler) popülerken; IS-IS, servis sağlayıcı (Türk Telekom, Vodafone vb.) ve devasa veri merkezi ağlarında daha çok tercih edilir çünkü genişlemesi biraz daha esnektir. İkisi de ağdaki en kısa yolu hesaplamak için Dijkstra algoritmasını kullanır.

#### Gateway Nedir?
Bir cihazdan `192.168.2.1`'e ping atmak istiyorsun. Cihaz önce şunu soruyor: _"Bu IP benim subnet'imde mi? Hayır ben `192.168.1.0/24` subnet'indeyim, hedef `192.168.2.1` subnet'inde. Bu benim subnet'imde değil."_ Bu durumda cihaz kendi subnet'i dışında ki bir hedefe paket göndermek istediğinde _"ben bunu bilemem, bir üst cihaza sorayım"_ diyor (bir üst cihaza soracak şekilde ayarlanmışsa). İşte o **üst cihaz** gateway oluyor. Yani gateway = _"bilmediğim her şeyi şuraya gönder"_ adresi. 

Örneğin GNS3'de bir VPCS cihazlarıyla çalışıldığında ve `ip 192.168.1.1/24 192.168.1.254` dediğinde:
- `192.168.1.1/24` → VPCS'nin kendi IP'si
- `192.168.1.254` → VPC cihazının baz alması gereken gateway cihazının adresi

Gateway cihazlarının subnet'in son IP'si olarak ayarlanmasının genel sebebi bir standart olarak kabul edilmesinden dolayıdır. Yani bir ağ da genel de son IP atanmış bir cihaz varsa gateway olarak kabul edilir.

#### Aynı subnet içinde ki uç cihaza gönderilen bir paketin yolculuğu
Burada her şey MAC adresleri ve ARP (Address Resolution Protocol) etrafında döner;

```
1. ARP Sorgusu: Cihaz A, Cihaz B'nin IP'sini bilir ama MAC adresini bilmez. Önce kendi ARP tablosuna bakar. Boşsa, ağa bir ARP Request (Broadcast) fırlatır.

2. Switch Öğrenme: Fiziksel switch, bu yayını alınca Cihaz A'nın MAC adresini ve hangi portta olduğunu MAC tablosuna yazar.

3. Hedef Yanıtı: Cihaz B, kendi IP'sini görünce ARP Reply (Unicast) döner.

4. İletim: Artık her iki cihaz ve switch birbirini tanıyor. Cihaz A, IP paketini Ethernet çerçevesine (frame) sarar ve switch üzerinden doğrudan B'ye gönderir.

5. Tablo Ömrü: Bu kayıtlar sonsuza kadar kalmaz. Genellikle MAC adresleri 300 saniye (5 dakika), ARP kayıtları ise işletim sistemine göre 2-20 dakika sonra tablodan silinir (aging).
```

#### Farklı subnet'te ki uç cihaza gönderilen bir paketin yolculuğu
```
1. Cihaz A hedef IP'ye bakıyor "10.0.0.5 benim subnet'imde mi?" → Hayır. O zaman paketi gateway'ime göndereceğim.

2. Gateway'in MAC adresini biliyor mu? ARP tablosuna bakar. Yoksa gateway'e ARP Request gönderir. Gateway MAC adresini ARP Reply ile döner. Cihaz A gateway'in MAC adresini öğrendi.

3. Paket hazırlanıyor
***************************************************
Hedef IP  → 10.0.0.5 (Cihaz B'nin IP'si, değişmez)
Hedef MAC → gateway'in MAC'i (Cihaz B'nin değil!)
***************************************************
Dikkat: IP adresi nihai hedefe ait ama MAC adresi sadece bir sonraki durağa ait.

4. Switch gateway'e iletir. Paketi alır, MAC tablosuna bakar, gateway'in portuna gönderir.

5. Router (gateway) paketi alır
*******************************************************************
- Layer 2 başlığına bakar → "Hedef MAC benim, bu paket benim için"
- Layer 2 başlığını söker, IP paketine bakar
- "Hedef IP 10.0.0.5, routing tablosuna bakayım"
- "10.0.0.0/24 subnet'i eth1'den erişilebilir"
*******************************************************************

6. Router yeni Layer 2 başlığı oluşturur
********************************************************
- Cihaz B'nin MAC adresini biliyor mu? Yoksa ARP sorar
- Yeni Ethernet frame:

Hedef IP  → 10.0.0.5 (hala aynı)
Hedef MAC → Cihaz B'nin MAC'i (artık değişti!)
Kaynak MAC → router'ın eth1 arayüzünün MAC'i
********************************************************

7. Cihaz B paketi alır
```

**Özet — Ne Değişiyor, Ne Değişmiyor:**

- IP adresleri  → baştan sona HİÇ değişmez
- MAC adresleri → her router atlamasında (hop) yeniden yazılır
 
 Her hop'ta MAC adresi "bir sonraki durak" oluyor — bu Layer 2 ve Layer 3'ün temel ayrımı.
#### Bir uç cihaza gateway ataması yaparken `default` argümanı ve onun haricinde gelebilecek argümanların anlamı

Gateway atamak için şu komut kullanılıyor:

```
ip route add default via 192.168.1.254
```

`default` kelimesi _"bilmediğin her şeyi şuraya gönder"_ demek. Bir docker host'unda uygulandığı varsayılırsa bu komutların aslında VPCS'de ki gateway atamasıyla aynı mantık, sadece komut farklı. Veya örneğin şöyle bir komut girdisi gelirse;

```
ip route add 192.168.2.0/24 via 192.168.1.254
```

Bu şunu söylüyor: "Sadece `192.168.2.0/24` subnet'ine gitmek istediğimde `192.168.1.254`'e gönder."

`default` ise bunun özel hali — "hiçbir rota eşleşmezse şuraya gönder" demek. Yani:

```
- Spesifik rota  → sadece o subnet için geçerli (sadece belirli bir subnet'in değerleri için 10.0.0.1'e paket yollanacaksa sadece o subnet'i geçerli yap 20.1.1.1 subnet'i için paket yollanamaz alınamaz)
default        → hiçbir şey eşleşmezse buraya git (10.0.0.1'de gelirse 20.1.1.1'de gelirse yani ne gelirse gelsin bilmediğim bir şey ise gateway'e yönlendir)

- `default` net_practice'de ki router'da yapılan konfigürasyonlarda hatırlanabilir. Network komutlarıyla (ip vb.) `default` argümanı daha iyi anlaşılmış oluyor.
```
#### Manuel yönlendirme örneği ve buna müteakip OSPF'in öneminin anlaşılması

Bir subnet'ten farklı bir subnet'e paket gönderimi yapılmak istendiğinde bunun için yönlendirme konfigürasyonu yapılması gerekir. GNS3'de şu şekilde bir topoloji örneği kurulduğunu tasavvur edelim;
```
VPCS-1 ── Router-1 ── Router-2 ── VPCS-2 
(VPC olmak zorunda değil normal docker uç cihazları da olabilir)
```

bu örnekte 3 subnet (3 kablomuz) var;
```
VPCS-1 --- [subnet 1] --- Router-1 --- [subnet 2] --- Router-2 --- [subnet 3] --- VPCS-2) 
```

Tüm bunlara şu şekilde bir ağ arayüzü ayarlaması yapılabilir;
```
VPCS-1: 192.168.1.1/24
Router-1 eth0: 192.168.1.254/24  (VPCS-1 tarafı)
Router-1 eth1: 10.0.0.1/30       (Router'lar arası)
Router-2 eth0: 10.0.0.2/30       (Router'lar arası)
Router-2 eth1: 192.168.2.254/24  (VPCS-2 tarafı)
VPCS-2: 192.168.2.1/24
```

Ağ arayüzlerini bu şekilde ayarladıktan sonra `VPCS-1`'den `VPCS-2` cihazına `ping 192.168.2.1` şeklinde `ping` atılmaya çalışıldığında başarız olunduğu görülebilir. `VPCS-1` cihazı `192.168.2.1` adresini `192.168.1.0` subnet'inde doğal olarak bulamadığından (farklı subnet'lere ait olmalarından) bu paketin üst bir cihaza (gateway'e) yönlendirilmesi gerek. Bunun için `VPCS-1`'de;

```bash
ip route add default via 192.168.1.254
```

aynı şekilde `VPCS-2` cihazından da `192.168.1.1` adresine ping atılmak istenebilir bu yüzden benzer yönlendirme yapılandırılması `VPCS-2`'de yine şu şekilde yapılabilir;

```bash
ip route add default via 192.168.2.254
```

Özetle;
```
1. Router-1'de:
   eth0 → 192.168.1.254/24
   eth1 → 10.0.0.1/30

2. Router-2'de:
   eth0 → 10.0.0.2/30
   eth1 → 192.168.2.254/24

3. VPCS-1'de:
   IP: 192.168.1.1/24
   Gateway: 192.168.1.254

4. VPCS-2'de:
   IP: 192.168.2.1/24
   Gateway: 192.168.2.254
```

`ip route add default via 192.168.1.254` komutuyla mevcut subnet'de adresi bulunamayan cihazın iletilmesi gereken paketlerini `192.168.1.254` IP adresine sahip cihaz aracılığıyla yönlendir diyoruz. Yine `ping` atmayı test edersek yine başarız olunduğu gözlemlenebilir. çünkü _Router-1_ cihazı da aynı şekilde yönlendirme yapması gerekli çünkü ona gelen bu yabancı paketlerin nereye ve nasıl yönlendirilmesi gerektiğini o da bilmiyor ona söylenmedi/yapılandırılmadı. Router-1'de buna mukabil olarak bu yabancı paketleri ona komşu olan diğer router'a yani _Router-2_'ye yönlendirmeli. Bu yüzden Router-1 cihazında bu komut uygulanabilir;

```bash
ip route add 192.168.2.0/24 via 10.0.0.2
```

kısacasi bu _192.168.2.0/24'e gitmek istersen Router-2'den geç_ diyor. Ayrıca aynı yapılandırmayı Router-2'de de yapmalıyız çünkü Router-2'den de Router-1'e bir geri dönüş **_respond_** paketleri gönderilecek. Bu yüzden Router-2'de benzer olarak;

```bash
ip route add 192.168.1.0/24 via 10.0.0.1
```

burada fark edileceği üzere `default` kullanılmadı. Ancak kullanılabilirdi. Router-1'de `... default via 10.0.0.2` yazarsan _"bilmediğin her şeyi Router-2'ye gönder"_ demiş olursun. Bu küçük topolojide işe yarar. Yani Router-1'de _"default via Router-2"_ yazarsan tüm bilinmeyen trafiği Router-2'ye gönderiyorsun. Router-2 paketi doğru yere iletebilir. Ancak;

```
VPCS-1 ── Router-1 ── Router-2 ── Router-3 ── VPCS-2
                          └── Router-4 ── VPCS-3
```

şu şekilde bir topoloji düşünürsek ve Router-1'de _"192.168.2.0/24 via Router-2"_ ve _"192.168.3.0/24 via Router-2"_ gibi spesifik rotalar yazarsan tam olarak hangi trafiğin nereye gideceğini biliyorsun daha kontrollü. Küçük ağlarda `default` pratik. Büyük ağlarda ise spesifik rotalar daha güvenilir. Bu mini tüyodan sonra `ping` komutu ile test yaparsak trafiğin başarılı olduğu gözlemlenebilir. Ek olarak VPCS-1 cihazından router-2'ye ping atılırsa; `ping 10.0.0.2` paketler neden ve nasıl başarılı şekilde hedefe (Router-2'ye) ulaşıyor?

VPCS-1 `10.0.0.2`'ye ping attığında şu oldu:

1. VPCS-1 _"10.0.0.2 benim subnet'imde mi?"_ → Hayır → Gateway'ime göndereyim → Router-1'e gidiyor
2. Router-1 _"10.0.0.2 nereye gider?"_ → Routing tablosuna bakıyor → `10.0.0.0/30` doğrudan bağlı, `eth1`'den çık → Router-2'ye ulaşıyor

Router-1'in zaten `10.0.0.0/30` subnet'ine doğrudan bağlı olması sayesinde mümkün kılınıyor. Az önce yapılandırması yapılan `ip route add 192.168.2.0/24 via 10.0.0.2, ip route add 192.168.1.0/24 via 10.0.0.1` ile mümkün kılınmadı. O iki komut ise şunun için gerekli: Router-1 `192.168.2.0/24`'ü bilmiyor, Router-2 `192.168.1.0/24`'ü bilmiyor. Bu komutlarla onlara _"o subnet bu yönde"_ dedik.

İşte OSPF'in bize sağladığı şey ise bu yönlendirme yapılandırmasını otomatize etmek; Şu an 2 router vardı ve 2 tane `ip route add` komutu yazdık — kolaydı. Ama şunu düşün: 100 router'lı bir ağda her router diğer 99 router'ın subnet'lerini bilmesi gerekiyor. 

Elle yazmak:
- Çok zaman alır
- Hata yapmak kolay
- Bir bağlantı kopsa veya yeni subnet eklenirse **her router'ı tek tek güncellemek** gerekir

OSPF bu işi otomatize ediyor:
- Yeni bir subnet eklendiğinde tüm router'lar otomatik öğreniyor
- Bir bağlantı kopunca routing tabloları otomatik güncelleniyor
- Sen hiçbir şeye dokunmak zorunda kalmıyorsun

Yani OSPF = manuel `ip route add` komutlarının otomatik ve dinamik versiyonu.

#### OSPF'in önemini anlamaya yönelik yapılabilecek manuel yönlendirme topoloji egzersizleri/pratikleri/örnekleri

1. Bu örnekte farklı subnet'lerde ki uç cihazlarin birbirlerine paket gönderirken Router-1 cihazinda nasil spesifik olarak yönlendirilmesi gerektiği ayarlaniyor;
```
        VPCS-1
          |
       Router-1
       /     \
Router-2    Router-3
   |           |
 VPCS-2      VPCS-3
```

2. Bu örnekte farkli subnet'e gidecek olan paketlerin hangi rotadan daha iyi gideceğinin ayarlamaları manuel olarak yapılıyor veya bağlanti kopma durumu oldugunda bu paketlerin alternatif hangi rotadan gitmesi gerektigi manuel olarak ayarlanmasi gerekiyor.
```
VPCS-1 ── Router-1 ── Router-2 ── VPCS-2
              |              |
           Router-3 ── Router-4
              |
           VPCS-3
```
_Topolojiyi ve yönlendirme yapılandırmaları yapıldıktan sonra her bir uç cihazin diğer uç cihazlara erişimini ping ile test edin. Hepsi birbirlerine düzgün şekilde ping gönderebiliyorlarsa Router-1 ile Router-2'nin bağlantısını kesin ve tekrardan birbirlerine ping atmayı deneyin. Başarısız olursanız bunu çözmeyi deneyin._

#### OSPF'e router'ların network adreslerini tanıtırken kullanılan `area 0`'ın anlamı nedir?

Çok büyük bir ağda yüzlerce router var. Hepsi birbirine OSPF ile bağlıysa her router tüm ağın haritasını tutmak zorunda — bu çok ağır olur. Area sistemi ağı **bölgelere** ayırıyor:

```
Area 0 (backbone)
    ├── Area 1
    ├── Area 2
    └── Area 3
```

Her area kendi içinde OSPF çalıştırıyor. Area'lar arası geçiş için **Area 0** merkez görevi görüyor — tüm diğer area'lar mutlaka Area 0'a bağlanmak zorunda. Peki `area 1` veya `area 2` yapsak ne değişir? Eğer bazı router'lar `area 0`, bazıları `area 1` derse — bu iki group birbirini göremez, aralarında özel bir **ABR (Area Border Router)** gerekir.
Bizim küçük topolojimizde tek area yeterli — hepsi `area 0`. Büyük ağlarda ise performans için birden fazla area kullanılır. OSPF'de her router komşularından _"ben şu subnet'lere sahibim"_ bilgisini alıyor. Bu bilgiler birikince router'ın aklında tüm ağın haritası oluşuyor.

Örneğin 100 router'lı bir ağda:
- Router-1, Router-2'den öğreniyor
- Router-2, Router-3'ten öğreniyor
- Bu zincir devam ediyor
- Sonunda Router-1 tüm 100 router'ın subnet bilgisine sahip

Buna **LSDB (Link State Database)** deniyor — her router'ın aklındaki ağ haritası. 100 router küçük bir ağ için sorun değil. Ama 10.000 router'lı bir ağda her router 10.000 router'ın bilgisini tutmak zorunda kalırsa — bu çok fazla bellek ve işlemci gücü demek.
Area sistemi bunu çözüyor: Router-1 sadece kendi area'sının haritasını tutuyor, tüm ağın değil.

##### Ama router tüm ağın haritasını tutması gerekli değil mi? Sonuçta en kısa rotayı veya bağlantı sorunu oldugu zaman alternatif rota ayarlaması yapması gerekli
Router'ın en kısa yolu bulması için haritaya ihtiyacı var. Ama; 10.000 router'lı dev bir ağda Router-1'in Japonya'daki bir router'ın detaylı haritasını bilmesi gerekiyor mu? Yoksa "Japonya'ya gitmek istersen şu yönden git" bilgisi yeterli mi? Area sistemi tam bunu yapıyor:

```
Area 1 (Türkiye)    Area 2 (Japonya)
    Router-1  ────────── ABR ────────── Router-500
```
Router-1 kendi area'sının detaylı haritasını biliyor. Japonya tarafı için sadece "ABR'den geç" biliyor — Japonya'nın iç detaylarını bilmesi gerekmiyor. Yani her şeyi bilmek yerine **yeterince** bilmek — bu area sisteminin özü.

#### OSPF `area` egzersizi

```
VPCS-1 ── Router-1 ── Router-2 ── Router-3 ── VPCS-2
```

Bu topoloji kurulup IP planlamasi yapıldıktan sonra OSPF'de şu şekilde ABR ayarı yapılabilir;

```
Router-1 ve Router-2 → Area 0
Router-2 ve Router-3 → Area 1
```

Bunun için;

Router-1;

```sh
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

```sh
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

```sh
vtysh
configure terminal
router ospf
network 10.0.0.4/30 area 1
network 192.168.2.0/24 area 1
exit
exit
write
```

Yapılandırmalar yapıldıktan sonra uç cihazlara ping gönderimini deneyin. Ardından Router-1 ve Router-3 cihazlarının kaç tane Router kaydı olduğunu görmek için Router yazılımındayken (vtysh'dayken);

```sh
show ip ospf database
```
veya
```sh
show ip ospf database router
```

### Wireshark GNS3 Entegrasyonu

#### Wireshark'ı GNS3 ile kullanma ve buna mütekakiben ağ trafiğini izleme

Herhangi bir topolojide ki ağ trafiğini izleyebilmek için ana makineye `wireshark` paketi kurulmalıdır. Kurulum sırasında `non-root users can capture packets` sorusu çıkacak — buna `Yes` deyin;

```sh
sudo apt install wireshark
```

Kurulum tamamlandıktan sonra GNS3'de ki bir topolojide iki cihaz arasinda ki kabloya sağ tıkla ve `start capture` seçeneğine tıkla. Bununla beraber Wireshark açılacak. Açıldıktan sonra bir router'ın terminalindeyken ping at veya OSPF çalışıyorsa zaten paketler görünmeye başlayacak.

#### Wireshark `Couldn't run dumpcap in child process: Permission denied` hatası

İzin sorununu çözmek için ana makine terminalinde;

```sh
sudo usermod -aG wireshark $USER
```

ve ana makineye `restart` at.
