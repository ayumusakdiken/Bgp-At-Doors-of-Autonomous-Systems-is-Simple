# BADASS

<img src="spiderweb.gif" align="right" height="500">

Bu proje de bir veri merkezi ağ altyapısının nasıl tasarlanması gerektiğinin temel pratik uygulamaları GNS3 programı ile simüle edilerek kurgu edilmesi istenmektedir. Aslında daha çok emüle etmek denilebilir. Bu sayede ağ yöneticiliği dünyası hakkında teorik olarak pek çok kavram ve yenilik edinilmiş olacak ve ayrıca pratik olarak da pek çok teknik ve çözümsel yaklaşımlar ile yeni perspektifler edinilmiş olacaktır. Teorik olarak internetin nasıl çalıştığı, özerk sistemlerin (AS) ne olduğu, ağ cihazlarının ne olduğu ve birbirleri ile olan etkileşimleri vb. örnekler verilebilir. Aynı şekilde az önce sıralanan edinimlerin pratik açıdan teknik anlam da arkaplan da nasıl çalıştığı ve nasıl dizayn edilmesi gerektiğinin öğrenilmesi hedeflenmektedir. Ancak ne olursa olsun teknik anlamda veri merkezlerinde oluşan sorunlar bizzat ve doğrudan yaşanılmadıkça bu sorunlar üzerine geliştirilen BGP EVPN, VLAN, VXLAN, VPLS, MPLS vb. teknik yaklaşımlarının tam anlamıyla anlaşılmasının zor olduğu kanaatindeyim. Bu yaklaşımlar ağ mühendisleri tarafından belirli sorunların üstesinden gelinmek amacıyla düşünülmüş ve geliştirilmiş tekniklerdir. Bu yüzden bu projenin bu tekniklerin nasıl kullanılması gerektiğini değil belirli sorunlar yaşanıldığında bu sorunların nasıl üstesinden gelinmesi gerektiğinin edinimini öğretmeyi hedeflemesi gerektiği kanaatindeyim. Bu model daha mühendissel/tekniker bir bakış açısı edinimi sağlayabilirdi. Ancak tabii bunun için bizzat saha da olmak gerekli ve bu mümkün olamadığından belki de bu proje bu kadarını bizlere sunmuştur. Bunların yanı sıra ağ kavramları çok soyut kavramlar olduğundan öğrenildiğini düşünülen şey bir anda farklı bir bağlam da çok farklı biçim de ele alınabilir. Bu da öğrenildiğini düşünülen şey hakkında gerçekten öğrenilip öğrenilmediğine dair şüpheler oluşturabilir. Bunu izah etmek gerekirse; Multicast'i üçgen olarak öğrendiğinizi varsayın (Multicast = üçgen). Ancak Multicast'i farklı bir bağlam da ele aldığınız da aslında Multicast'in kare olduğunu öğreniyorsunuz. Daha sonra yine farklı bir bağlam da ele aldığınızda aslında Multicast yıldızmış. Tüm bunlar fark edildiğinde Multicast'in bağlamsal duruma göre hem teknik hem de ifadesel olarak esnek bir kavram olduğu sonucuna varabilirsiniz. Bu C'de pointer öğrendiğinizi zannetmenize örnek verilebilir :d. Farklı bir kimseden pointer konusunu dinlediğinizde zihninizde ki kavramla örtüşmediğini ancak pointer'ı anlatan kimsenin de çok tutarlı bir şekilde izahat de bulunduğunu fark edip hangisinin doğru olduğunun sorgulamasına düşebilirsiniz. Bu hem siz hem de diğer kimsenin pointer'ı kavramını zihin de nasıl ilişkilendiriğine bağlı bir durumdur. Her iki kişi de zihnin de pointer kavramını tutarlı bir biçim de ilişkilendirmiş ama bunu birbirlerine anlatmaya çalıştıklarında örtüşmediğini fark ederler. Ama günün sonunda aslında aynı şeyden bahsediyorlardır. Özetle belki de tüm bunların sebebi ağ kavramlarının bağlamsal ve anlamsal olarak iç içe geçmesi ve tam anlamıyla bir literatür standardı oluşturulamaması durumu yüzünden her üretici (Cisco, Juniper, FRR vb.) kendi terminolojisini ve isimlendirmesini kullanıyor bu da karmaşıklığın artmasına daha da sebep oluyor.

Bu yazı da tıpkı proje dokümanında olduğu gibi bölüm bölüm ve her bölüm bir öncekinin devamı niteliğinde bir ilerleme yapılacaktır. Her bölüm de karşılaşılan sorunlar dile getirilecek ve bunlara yönelik ne gibi çözümler uygulanabileceği açıklanacaktır. Ayrıca sadece sorun - çözüm odaklı değil proje dokümanın da belirtildiği üzere incelenmesi istenilen kavramların notları da bulunmaktadır. Bu yazının kendisi de internet üzerinde ki herhangi bir kaynaktır ve burada ki açıklamaların mutlak doğru olduğu iddiası yoktur. İlk paragrafta da belirtildiği üzere benim üçgen olarak açıkladığım bir şeyi sizler kare olarak açıklayabilir ve bu çok mantıklı ve tutarlı olabilir. Tıpkı üçgenin bana mantıklı ve tutarlı hissettirmesi gibi. Ama aslında aynı şeyden bahsediyor olabiliriz yani ortada bir şekil olduğu gerçeğinden. 

## İçindekiler
  - [Part 1](#part-1)
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
  - [Part 2](#part-2)
    - [Router ve Switch cihazlarının birbirlerinden asıl farkları](#router-ve-switch-cihazlarının-birbirlerinden-asıl-farkları)
    - [Ağ teriminin geniş ve bağlama göre değişkenlik gösterebilir (formlanabilir) cinste bir kavram oluşu üzerine](#ağ-teriminin-geniş-ve-bağlama-göre-değişkenlik-gösterebilir-formlanabilir-cinste-bir-kavram-oluşu-üzerine)
    - [VLAN nedir?](#vlan-nedir)
    - [Layer 3 cihazları ile mantıksal olarak ağ segmenlendirilmesine rağmen neden Layer 2 katmanında bu sorun çözülmeye çalışılmıştır?](#layer-3-cihazları-ile-mantıksal-olarak-ağ-segmenlendirilmesine-rağmen-neden-layer-2-katmanında-bu-sorun-çözülmeye-çalışılmıştır)
    - [VLAN egzersizi](#vlan-egzersizi)
    - [Gerçek senaryo da VLAN ağ dilimlemesi teknik olarak nerede ve nasıl yapıyor? Ayrım tam olarak nerede yapılıyor konfigüre ediliyor?](#gerçek-senaryo-da-vlan-ağ-dilimlemesi-teknik-olarak-nerede-ve-nasıl-yapıyor-ayrım-tam-olarak-nerede-yapılıyor-konfigüre-ediliyor)
    - [VLAN'ın teknik sınırları ve yetersizliği](#vlanın-teknik-sınırları-ve-yetersizliği)
    - [VXLAN nedir?](#vxlan-nedir)
    - [VLAN ile VXLAN'ın konfigürasyonel farklılıkları](#vlan-ile-vxlanın-konfigürasyonel-farklılıkları)
    - [VXLAN'ın İşleyişi](#vxlanın-i̇şleyişi)
    - [Uç cihazlar Layer 3 katmanında çalışan cihazlar ise nasıl Layer 2 paketi gönderebiliyorlar?](#uç-cihazlar-layer-3-katmanında-çalışan-cihazlar-ise-nasıl-layer-2-paketi-gönderebiliyorlar)
    - [Statik mod ile temel ve basit bir VXLAN topoloji örneği](#statik-mod-ile-temel-ve-basit-bir-vxlan-topoloji-örneği)
    - [Unicast, Multicast, Broadcast nedir?](#unicast-multicast-broadcast-nedir)
    - [Unicast, Multicast ve Broadcast bunlar cihaz tarafından arkaplanda otomatik olarak gerceklestirilen mekanikler. Örneğin bir cihazin unicast veya multicast olarak davranması gerektiği nasıl belirtiliyor?](#unicast-multicast-ve-broadcast-bunlar-cihaz-tarafından-arkaplanda-otomatik-olarak-gerceklestirilen-mekanikler-örneğin-bir-cihazin-unicast-veya-multicast-olarak-davranması-gerektiği-nasıl-belirtiliyor)
    - [`224.x.x.x` ile `239.x.x.x` arası multicasting yapabilmek için özel olarak ayrılmış IP adresleri](#224xxx-ile-239xxx-arası-multicasting-yapabilmek-için-özel-olarak-ayrılmış-ip-adresleri)
    - [Broadcast ve ARP ilişkisi nedir? Bir cihaz ne zaman ARP atar? ARP her zaman mı atılır yoksa gerektiğinde mi? Gerektiği zaman ne zaman?](#broadcast-ve-arp-ilişkisi-nedir-bir-cihaz-ne-zaman-arp-atar-arp-her-zaman-mı-atılır-yoksa-gerektiğinde-mi-gerektiği-zaman-ne-zaman)
    - [Unicast, Multicast, Broadcast vb. mekaniklerin pratik olarak denenebilirliği için uygun protokolü kullanan bir aracın gerekliliği üzerine](#unicast-multicast-broadcast-vb-mekaniklerin-pratik-olarak-denenebilirliği-için-uygun-protokolü-kullanan-bir-aracın-gerekliliği-üzerine)
    - [Multicast modu ile temel ve basit bir VXLAN topoloji örneği](#multicast-modu-ile-temel-ve-basit-bir-vxlan-topoloji-örneği)
    - [Bir ağ interface'inin detaylarını daha da fazla görme komutu](#bir-ağ-interfaceinin-detaylarını-daha-da-fazla-görme-komutu)
    - [Sanal ağ arayüzlerinin paket iletimi üzerine](#sanal-ağ-arayüzlerinin-paket-iletimi-üzerine)
    - [Bir ağ arayüzüne (eth0, eth1 vb.) birden fazla IP adresi nasıl atanabiliyor? Ve durum böyle ise o halde bir cihazın birden fazla port'unun olmasının ne anlamı ve gereği var?](#bir-ağ-arayüzüne-eth0-eth1-vb-birden-fazla-ip-adresi-nasıl-atanabiliyor-ve-durum-böyle-ise-o-halde-bir-cihazın-birden-fazla-portunun-olmasının-ne-anlamı-ve-gereği-var)
    - [Bridge ağ arayüzüne bağlı port'ların incelenmesi](#bridge-ağ-arayüzüne-bağlı-portların-incelenmesi)
    - [VXLAN'ın statik modda (unicast) veya dinamik multicast modda ayarlanması sonucunda bu modların farklari ve üstlendikleri roller](#vxlanın-statik-modda-unicast-veya-dinamik-multicast-modda-ayarlanması-sonucunda-bu-modların-farklari-ve-üstlendikleri-roller)
    - [Uç cihazdan gönderilen bir paketin VXLAN yapılı ağda ki yolculuğu](#uç-cihazdan-gönderilen-bir-paketin-vxlan-yapılı-ağda-ki-yolculuğu)
  - [Part 3](#part-3)
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
  - [Proje Teslimi ve Organizasyonu](#proje-teslimi-ve-organizasyonu)
  - [Kaynaklar](#kaynaklar)

## Part 1
Bu bölüm de mevcut sisteme GNS3'ün nasıl kurulacağını ve ona Docker entegrasyonunun nasıl gerçekleştirilmesi gerektiği açıklanacaktır. Ayrıca GNS3'ün nasıl kullanılması gerektiği ve programda ki terminolojinin ne anlama geldiği tarzında açıklamalar yapılacaktır.
### GNS3 Kurulum Sorunları ve Çözümleri
Proje dokümanında projenin bir sanal makine de yapılması isteniliyor. Ayrıca GNS3 ve onun bağımlılık paketleri mevcut sisteminizi gereksiz yere şişirip kirletebileceğinden tüm işlemleri bir sanal makine de yapmak en iyisi olacaktır. Tüm işlemler **Debian 13** üzerinden yürütülmüştür. Bu yüzden GNS3 kurulumu esnasında yaşanan sorunların bir kısmı Debian 13 ile ilgilidir. Bu yüzden sanal makineye Debian 13 yükleyip GNS3 kurulumu yapmaya çalışan kimselerin burada ki sorunları yaşaması muhtemeldir.

#### `dynamips` ve `software-properties-common` paketleri sorunu
GNS3'ün resmi web sitesinden Debian ve Debian tabanlı dağıtımlar için GNS3 ve ona gerekli olan bağımlılık paketlerini yüklemeye çalışırken bağımlılık hatası alınır. Debian 13 ve Debian 13 tabanlı dağıtımlarda, `dynamips` ve `software-properties-common` paketleri `apt` deposundan kaldırılmıştır; bu nedenle, `dynamips` olmadan yükleme yapıp ardından `dynamips`'i ayrı olarak yükleyeceğiz. Önce resmi web sitesinde ki yükleme adımlarında ki komut satırından `dynamips` ve `software-properties-common` paketlerini kaldırıp GNS3 için gerekli paketleri sisteme yükleyin;

```
sudo apt install python3 python3-pip pipx python3-pyqt6 python3-pyqt6.qtwebsockets python3-pyqt6.qtsvg qemu-kvm qemu-utils libvirt-clients libvirt-daemon-system virtinst ca-certificates curl gnupg2 
```

Şimdi `dynmaips` paketini ayrı olarak sisteme yükleyin;

```
wget http://ftp.us.debian.org/debian/pool/non-free/d/dynamips/dynamips_0.2.14-1_amd64.deb
```

ardından;

```
sudo dpkg -i dynamips_0.2.14-1_amd64.deb
```

Bunun ardından resmi web sitesinde ki `pipx` ile GNS3 server ve GUI'ı kurma adımından devam edebilirsiniz.

#### `No busybox executable could be found, please install busybox (apt install busybox-static on Debian/Ubuntu) and make sure it is in your PATH` hatası

Bu hata genelde GNS3’ün çalıştığı sistemde busybox bulunamadığında çıkar — yani sorun çoğu zaman Docker image içinde değil, GNS3 Server’ın kurulu olduğu ana makinede.

Busybox'ı kur:
```
sudo apt update
sudo apt install busybox-static
```

Kurulduğunu doğrula:
```
which busybox
```

Eğer çıktı:
```
/usr/bin/busybox
```

şeklindeyse tamamdır.

#### VPCS ağ cihazları ile ilgili hatalar
##### `No path to a VPCS executable has been set` hatası
VPCS cihazlarını topolojinizde kullanmaya çalıştığınızda bu hata GNS3 tarafından verilebilir. Bunun sebebi ana sisteme `vpcs` paketinin kurulu olmamasından kaynaklıdır;

```
sudo apt install vpcs
```

##### `VPCS executable version must be >= 0.6.1 but not a 0.8` hatası
`vpcs` paketini sisteme kurup tekrardan topolojiyi ayağa kaldırmaya çalıştığınızda bu seferde bir _**version missmatch**_ hatası alabilirsiniz. Bunu çözmek için versiyonu yüksek olan `vpcs` paketini kaynak koddan derleyip sisteme yüklemek gereklidir bunun için;

```
wget https://github.com/GNS3/vpcs/archive/refs/tags/v0.8.3.zip
```

indirdikten sonra, `.zip` dosyasını açın ve içinde ki `src` klasörüne gidin;

```
cd v0.8.3/src
```

ardından VPCS scrpit'ini çalıştırmak için aşağıdaki komutu çalıştırın bu kaynak dosyaları derleyecektir;

```
./mk.sh
```

derleme işlemi tamamlandığında, VPCS'nin eski sürümünü kaldırın;

```
sudo rm /usr/bin/vpcs
```

Ardından yeni versiyonu `/usr/bin/` dizinine kopyalayın. Örneğin:

```
sudo cp /home/$USER/v0.8.3/src/vpcs /usr/bin/vpcs
```

#### GNS3 `uBridge not avaiable` hatası

Debian 13'te uBridge paketi depoda bulunmadığından, **kaynak koddan derleme** gerekiyor. Bunun için önce gerekli bağımlılıkları kurman, sonra GitHub'dan paketi indirip derlemen gerekiyor;

Öncelikle gerekli bağımlılıkları sisteme kur;

```
sudo apt install git build-essential libpcap-dev -y
```

ardından uBridge'i Github'dan çek ve derle;

```
git clone https://github.com/GNS3/ubridge.git
cd ubridge
make
```

derleme tamamlandıktan sonra sisteme uBridge'i kur;

```
sudo make install
```

uBridge `/usr/local/bin/ubridge` konumuna kurulacaktır.

Ardından uBridge'e ağ yetkilerini ver;

```
sudo setcap cap_net_admin,cap_net_raw=ep /usr/local/bin/ubridge
```

kullanıcını gruplara ekle;

```
sudo usermod -aG wireshark $(whoami)
```

Sistemi yeniden başlat;
```
sudo reboot
```

Kurulumu doğrula;
```
ubridge --version
```

Çıktı olarak `uBridge version 0.9.x` gibi bir şey görürsen kurulum başarılıdır. Ardından GNS3'ü aç, hata gitmiş olmalı. Sorun devam ederse GNS3 içinde `Edit → Preferences → Server` kısmında uBridge yolunu `/usr/local/bin/ubridge` olarak manuel ayarla.

#### GNS3 SIP Module ve QT sorunu
`pipx` ile kurulan GNS3, eksik sistem kütüphaneleri nedeniyle başlamayabilir;
- GNS3'ün yeni sürümleri PyQt5 değil **PyQt6** gerektiriyor
- `pipx` izole ortam oluşturduğu için PyQt6'yı manuel inject etmek gerekiyor
- Debian 13 minimal kurulumda PyQt6'nın ihtiyaç duyduğu **XCB kütüphaneleri** varsayılan olarak gelmiyor

Çözüm için;

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
GNS3'te router cihazina verilen **adapter** sayısı o cihaza kaç cihazın bağlanılabileceğini belirtir. Örneğin; **_2 adapter_** derken GNS3'ün o container'a kaç tane sanal ethernet portu vereceğini belirliyoruz. Yani; Fiziksel bir router satın aldığında üzerinde kaç ethernet portu varsa o kadar cihaza bağlanabiliyorsun. GNS3'de adapter sayısı tam olarak bu. O sanal router'ın kaç ethernet portuna sahip olacağını belirliyor. Yani bu yüzden `ip a` komutunun çıktısı olarak **2 adapter = 2 ethernet portu = eth0 ve eth1** arayüzü görüyorsun.
#### GNS3 Web Client ile Web üzerinden GNS3 çalıştırmak
GNS3 yazılımı iki parçadan oluşuyor; GNS3 GUI (client kısmı) ve GNS3 server kısmı.
GNS3 server asıl işi yapan kısım. Container'ları başlatıyor, bağlantıları kuruyor, trafiği yönetiyor. GUI ise sadece görsel arayüz. İkisi ayrı olduğundan GNS3 server uzak bir makinede de çalışabilir. Herhangi bir PC'de ki GNS3 GUI (cilent) ile bağlanırsın ve bu ayrım sayesinde GNS3'ün server kısmını uzak bir sunucuya kurup bunu dışarıdan erişilebilir hale getirdikten sonra herhangi bir GNS3 client'ından bu server'a bağlanarak GNS3 çalıştırılabilir hale getirebilirsin. Ortak çalışmalar için kullanışlı bir çözüm olabilir.
#### GNS3'ün modüler bir yazılım olması üzerine
GNS3 bir simülasyon programı ise router, end devices vb. ağ cihazlarını ve öğelerini hazır olarak barındırması gerekmez mi? Neden bazı ağ cihazları mevcut iken (ethernet switch, VPCs vb.) bazı ağ cihazları (routers vb.) GNS3 içerisinde hazır olarak mevcut değil? Tarzında soru sorulabilir. Bunun cevabı GNS3'ün tasarım biçimindedir. GNS3'ün tasarım hedefi şu: "Ben sadece topolojiyi yöneteyim, cihazları sen oluştur ve içini sen doldur." Bunun avantajı esneklik — istediğin router yazılımını, istediğin işletim sistemini kullanabiliyorsun. Eğer GNS3 her şeyi içine gömseydi hem çok büyük olurdu hem de her yeni teknoloji için GNS3'ü güncellemen gerekirdi. İşte bu sayede GNS3'ün Docker ile entegrasyonuyla istenilen imajlar ile istenilen ağ cihazı oluşturulabilir ve bu GNS3'e entegre edilip ağ topolojilerinde kullanılabilir hale getirilebilir. Docker'ın yanı sıra VPCS gibi PC simulasyon araçlarının kullanılabilmesinin sebebi tamamen GNS3'e entegre edilmesidir. Yani ana makinenize `vpcs` paketini yüklemediyseniz GNS3'te bu mini PC simülatörlerinin kullanımı mümkün değildir. Bunlar GNS3'e has gömülü ağ cihazları değildir. Tıpkı Docker'da olduğu gibi entegre edilmesi gereken araçlardır. Yani `vpcs` paketini GNS3 haricinde de ana makineye yükleyip kullanabilirsiniz bir bağımlılığı yoktur. 
#### Proje dokümanında öğreticilik açısından kasıtlı olarak yapıldığını düşündüğüm busybox kafa karıştırması
Proje dokümanında docker image'ler de **busybox** veya ona eşdeğer bir paketin mevcut bulunması istendiği belirtiliyor. Bu ayarlanıp bir topoloji ayağa kaldırılmaya çalışıldığı zaman GNS3 `no path busybox..` hatası veriyor. Bu hata alındığında proje de docker image'ler de bulunulması istenilen **busybox** paketi ile ilgili bir anlığına sorun yaşanıldığı sanılabiliyor. Ancak sorunun bununla bir ilgisi olmadığının bilinmesi gerek. Çünkü ana makine de `gns3server` docker konteynerlarını ayağa kaldırmadan evvel birkaç hazırlık yapması gerekiyor ve bunları belirli script'ler aracılığıyla sağlıyor. Bu script'lerde de busybox komutları kullanıldığından aslında ana makinenin `busybox` paketine sahip olması gereklidir. Sorunun docker image'lerde yüklenmeye çalışılan busybox paketiyle bir ilgisi yoktur. Bu yanılgıya düşülmemelidir. GNS3'ün bu script'ler de busybox kullanmasının sebebi de `gns3server`'ın yapacağı hazırlıkların her farklı işletim sistemin de aynı şekilde çalışmasını sağlamak üzerine olduğundandır. Çünkü farklı Linux işletim sistemlerinde temel Linux komutları (ls, cp, mv vb.) farklı davranışlar sergileyebildiğinden `gns3server`'ın hazırlığı farklı sonuçlar verebilir. Bunun olmaması için her farklı makine de aynı davranışlar ile aynı hazırlıkların mümkün kılınabilmesi için busybox kullanılmaktadır. Çünkü busybox komutlarının tipik davranışı olarak işletim sistemi farklı da olsa aynı davranışları sergileyecektir.

GNS3'ün hazırlık script'lerinden `init.sh` script'i şöyle başlıyor:
```
#!/gns3/bin/busybox sh
```

İşte tam bu yüzden proje dokümanında docker image'lerine `busybox` kurdurması tamamen kafa karışıklığı yaratmak için ancak bu kafa karışıklığını yaratılmak istenmesinin sebebi kasıtlı. Bu kasıt GNS3'ün altyapısında `busybox`'ın nasıl kullanıldığını öğretmek/anlatmak için. Container içerisine kurduğumuz `busybox` ile ilgili hiçbir ilişiği yok. Yani proje bizden image'lerde busybox istemeseydi de bizim ana makinemize busybox kurmamız gerekecekti çünkü GNS3'ün ihtiyacı var hazırlık script'leri için. Bu da onun bağımlılık paketi olduğu anlamına geliyor. 
#### Docker konteynerlar çalıştıktan sonra içlerinde barındırılan `/gns3` klasörü ve script'leri
Docker imajları ile oluşturulmuş ağ cihazlarının GNS3'de ki bir topoloji de kullanılıp bu topoloji ayağa kaldırıldıktan sonra bu ağ cihazlarının terminal ortamına girildiğinde `/gns3` ve bu klasörün içerisinde yine GNS3 hazırlık script'leri görülebilir. Bu klasör ve script'lerin neden halen içlerinde barındırıldığına dair bir soru yöneltilecek olursa; Bu scriptler GNS3 server ile container arasındaki köprü olmasındandır. Kabaca düşünülecek olursa konteynerda yapılan değişikliklerin (ip adresi atama ve diğer benzeri konfigürasyonlar) haberi `gns3server`'a iletilmesi gerekli ki `gns3server`'da bunu işlesin ve GNS GUI'da bunu yansıtsın. Bu yüzden bu script'ler konteyner'a mount ediliyor. Ve temel olarak GNS3 server her container'ı başlatırken kendi `init.sh` scriptini container'a mount ediyor. Bu script şunları yapıyor;

- Ağ arayüzlerini ayarlıyor (örneğin kaç adet adapter sayısı verdiysek o kadar arayüz oluşturma)
- Telnet bağlantısını hazırlıyor (terminal ile makineyle iletişim kurabilmek için)
- GNS3'ün container'ı yönetebilmesi için ortamı hazırlıyor

Kabaca genel yapı;
```
GNS3 GUI → GNS3 Server → init.sh (host busybox ile çalışır) → Container başlar → Telnet ile terminal açılır
```

Script'ler için `/gns3` klasöründe ki `bin` klasörünün altında ki `busybox` kullanılıyor. Bunu da ana makineden kopyalıyor. Ayrıca madem `/gns3` klasörü docker konteynerına kopyalanıyor ve bununla beraber ana makinede ki `busybox` aracıda kopyalanmış oluyor o zaman buna müteakip şöyle bir trick ve optimizasyon yapilabilir; GNS3 zaten konteynerde ki `/gns3` klasörüne busybox'i kopyaladığından ötürü Docker image'e ekstradan bir daha busybox paketinin kurulmasına gerek yoktur. Ancak buna uygun bir Dockerfile veya Dockerfile'ın çalıştıracağı bir script hazırlanması gerekli ki konteyner `/gns3/bin/busybox` dizininde ki busybox'i uygun şekilde çalıştırdın aksi taktirde nedeni bilinmeyen şekilde konteyner hemen `exited` durumuna düşüyor. Script'in nasıl hazırlanması gerektiğine ipucu olarak proje dokümaninda Part 1 bölümünde ki görseller incelenebilir. Uygun script hazırlandığı taktirde proje dokümanında ki busybox isteğini karşılar nitelikte olur ve konteyner daha optimize olur.
### Temel Ağ Kavramları
#### `ip a` komutunun çıktısında gözüken ağ arayüzlerinin anlamları
`ip a` (veya `ip addr`) komutu mevcut cihazın **ağ arayüzlerini** gösteriyor. Şöyle ki: Fiziksel bir bilgisayarda ağ kartı var — ethernet portu, Wi-Fi kartı gibi. Bunların her biri bir ağ arayüzü. `eth0`, `eth1` bunların sanal karşılıkları/temsilleri — her biri bir ethernet portu. Bağladığın her kablo bir `eth` arayüzüne denk geliyor. `lo` ise **loopback** — fiziksel bir port değil, cihazın kendisiyle konuşması için özel bir sanal arayüz. `127.0.0.1` adresi hep buraya ait. `enp` öneki ile başlayan isimler ise daha yeni Linux sistemlerde kullanılan isimlendirme standardı — `eth0` yerine donanımın fiziksel konumuna göre isim veriliyor.
#### Router yazılımı ne demek? Router yazılımı bir cihaza indirildiğinde ne oluyor?
Fiziksel olarak bir router ile normal bir bilgisayar arasında aslında çok fark yok — ikisi de bir işlemci, RAM, ağ kartlarından oluşuyor. Fark şurada: **router yazılımı.**

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

Yani "router" aslında bir donanım değil, bir **rol** — ve bu rolü yazılım belirliyor. Bu yazılım makineye kurulduğunda makine router nitelikli hale formlandırılabilir demek oluyor. Bir Laptop, mobil cihaz üzerine router yazılımı kurulabiliyorsa bu cihazlarda router cihazı gibi davrandırılabilir. Cisco, Juniper gibi şirketlerin router'ları da özünde aynı şey — özel donanım üzerinde çalışan router yazılımları. FRR ise bu yazılımın açık kaynaklı versiyonu.

#### FRR yazilim çatısı altında ki diğer yazılımların işlevleri
Zebra ve Quaagga FRR'nin koordinatörleri ancak aktif olarak FRR'da **zebra** kullanıldığından zebra routing tablosunu yönetiyor. Diğer tüm servisler (ospfd, bgpd, isisd) öğrendikleri rota bilgilerini zebra'ya bildiriyor, zebra bunları Linux kernel'in routing tablosuna yazıyor. Zebra olmadan diğer servisler kernel ile konuşamıyor. Manuel olarak `ip route 192.168.1.0/24 10.0.0.1` yazıldığında, işletim sistemi çekirdeğine (Kernel) doğrudan emir verirsin. Tek tek `ip route` yazmak yerine; Zebra, protokollerden gelen dinamik bilgileri kullanarak o `ip route` komutlarını saniyeler içinde ve sürekli güncelleyerek otomatik olarak takip eder ve arka planda çalıştırır. Zebra bu durumu otomatik hale getirir;

- Haber Toplama: BGP veya OSPF gibi protokoller, komşu cihazlardan _"Şu ağ bende var!"_ bilgisini alır.
- Karar Verme: Zebra bu bilgileri toplar. Eğer aynı yere giden iki yol varsa, en iyisini seçer.
- Uygulama: Zebra, seçtiği en iyi rotayı senin yerine otomatik olarak işletim sisteminin yönlendirme tablosuna (Kernel/FIB) yazar.

**Quagga** ise FRR'nin eski hali. Artık aktif geliştirilmiyor. FRR, Quagga'dan fork edildi ve devam etti. Proje dökümanında _"zebra veya quagga"_ diyor çünkü ikisi de aynı işi yapıyor, sadece biri eski biri yeni.

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

```
ip route add default via 192.168.1.254
```

aynı şekilde `VPCS-2` cihazından da `192.168.1.1` adresine ping atılmak istenebilir bu yüzden benzer yönlendirme yapılandırılması `VPCS-2`'de yine şu şekilde yapılabilir;

```
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

```
ip route add 192.168.2.0/24 via 10.0.0.2
```

kısacasi bu _192.168.2.0/24'e gitmek istersen Router-2'den geç_ diyor. Ayrıca aynı yapılandırmayı Router-2'de de yapmalıyız çünkü Router-2'den de Router-1'e bir geri dönüş **_respond_** paketleri gönderilecek. Bu yüzden Router-2'de benzer olarak;

```
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

Yapılandırmalar yapıldıktan sonra uç cihazlara ping gönderimini deneyin. Ardından Router-1 ve Router-3 cihazlarının kaç tane Router kaydı olduğunu görmek için Router yazılımındayken (vtysh'dayken);

```
show ip ospf database
```
veya
```
show ip ospf database router
```

### Wireshark GNS3 Entegrasyonu

#### Wireshark'ı GNS3 ile kullanma ve buna mütekakiben ağ trafiğini izleme

Herhangi bir topolojide ki ağ trafiğini izleyebilmek için ana makineye `wireshark` paketi kurulmalıdır. Kurulum sırasında `non-root users can capture packets` sorusu çıkacak — buna `Yes` deyin);

```
sudo apt install wireshark
```

Kurulum tamamlandıktan sonra GNS3'de ki bir topolojide iki cihaz arasinda ki kabloya sağ tıkla ve `start capture` seçeneğine tıkla. Bununla beraber Wireshark açılacak. Açıldıktan sonra bir router'ın terminalindeyken ping at veya OSPF çalışıyorsa zaten paketler görünmeye başlayacak.

#### Wireshark `Couldn't run dumpcap in child process: Permission denied` hatası

İzin sorununu çözmek için ana makine terminalinde;

```
sudo usermod -aG wireshark $USER
```

ve ana makineye `restart` at.


## Part 2
Bu bölüm aynı ağda ki (aynı subnet) cihazların birbirlerinden nasıl izole edilebilceğini yani ağı nasıl dilimlere/bölümlere ayrılabileceği açıklanmakta ve ayrıca farklı subnet'lerde (uzak ve farklı lokasyonlarda) bulunan cihazların sanal bir ağ katmanı aracılığıyla nasıl sanki aynı ağdaymış (subnet) gibi davrandıkları açıklanacaktır.
### Router ve Switch cihazlarının birbirlerinden asıl farkları
OSI modeli (ağ iletişimini katmanlara bölen model) bazında **Router Layer 3** katmanında çalışır ancak **Switch Layer 2** katmanında çalışır.

```
Layer 2 → MAC adresi → Switch'in dünyası
Layer 3 → IP adresi  → Router'ın dünyası
```

Switch subnet'leri anlamıyor. Switch sadece MAC adresi ile çalışıyor — _"bu MAC adresi bu porta bağlı"_ diyor ve paketi oraya gönderiyor. IP adresine, subnet'e bakmıyor. Kısaca Switch'e bağlı cihazları mantıksal olarak segmentlere bölsek de (subnet'leme) Switch tamamen farklı bir çerçeve içinde çalıştığından (MAC adresine göre) bu yapılandırmadan bir haber şekilde sadece ona gelen paketlerin kime iletileceğini kendi ağında mevcut mu diye bakarak paketleri ona gönderecek eğer kendi ağındaysa (yani bu cihazlar bu Switch'e bağlıysa). Switch ağın merkezi/kökü gibi düşünülebilir. Cihazlar doğrudan birbirlerine bağlanıp da bir ağ oluşturabilirdi. Ancak bazı ağlar merkezi bir aracı (switch) ile de oluşturulabilir. Switch cihazların MAC adreslerine bakıp paket iletimi yaptığından IP protokolü ile çalışmaz. Sadece üzerine bağlı cihazlar arasında iletişimi sağlar. Teorik açıdan bakıldığında sanki switch'e bağlı tüm cihazlar birbirlerine `ping` atabilir iması oluşuyor olabilir (yani `192.168.1.1` IP'li cihaz `10.0.0.1` cihazına paket gönderebilir iması gibi). Ancak bu tamamen yanlış bir ima ve zan olacaktır. Çünkü Switch IP ile değil, MAC adresi ile çalışır bu doğru bir ifadedir ama hostlar (uç cihazlar) IP katmanında (Layer3) karar verir. Bu yüzden cihaz (host) pratik de _"`10.0.0.1` benim subnet'im de değil - ya gateway'e göndermeliyim - ya da gönderemem (gateway yoksa)"_ daha yola bile çıkamaz (mantıksal olarak) aynı subnet'de olmadığından. Burada ARP davranışını unutmamak gerekli. ARP davranışı:

- Aynı subnet → ARP atılır → MAC öğrenilir → switch iletir
- Farklı subnet → ARP atılmaz bile, gateway aranır -> o da yoksa paket host'dan dışarı dahi çıkamaz.

bu yüzden farklı subnet’teki iki cihaz doğrudan konuşamaz. _“Switch iletir”_ söylemi neden kafa karıştırıyor? Şu durum için doğru; Switch, kendisine gelen frame’i MAC’e göre iletir ama frame’in oluşması için önce IP katmanı karar vermeli yani Switch _“her şeyi iletir”_ değil _“kendisine gelen şeyi iletir”_. Peki neden sadece MAC adreslerine bakıp cihazlar arası iletişimi sağliyor diye bir soru sorulursa bu tamamen bu cihazin bu sekilde çalışılması istendiğinden dolayı bu şekilde tasarlanmış olduğu şeklinde cevap verilebilir :d

```
Switch → Aynı ağdaki cihazları birbirine bağlar. "Sen ve ben aynı ağdayız, direkt konuşabiliriz." (`192.168.1.0/24` ağında ki tüm cihazlar switch'i kullanarak birbirleriyle iletişim kurabilir)

Router → Farklı ağlar arasında köprü kurar. "Sen farklı ağdasın, sana ulaşmak için yönlendirme gerekiyor." (192.168.1.1/24 ile 192.168.2.1/24 farklı ağlarını birbirine bağlar)
```

```
(192.168.1.0/24 ağı) [PC1] (192.168.1.1) --- Switch --- Router --- Swich --- (192.168.2.1) [PC2] (192.168.2.0/24 ağı)
```

### Ağ teriminin geniş ve bağlama göre değişkenlik gösterebilir (formlanabilir) cinste bir kavram oluşu üzerine

Ağ kavramı çok geniş ve bağlama göre değişkenlik gösterebilir cinsten bir terim olduğundan şunlar belirtilmeli;

**Aynı ağ = aynı subnet** demek. Yani `192.168.1.0/24` subnet'indeki tüm cihazlar _"aynı ağda"._ Bu cihazlar birbirleriyle direkt konuşabiliyor — router'a gerek yok, switch yeterli.

**Farklı ağ = farklı subnet** demek. `192.168.1.0/24` ile `192.168.2.0/24` farklı ağlar. Bu iki ağ arasında iletişim için router gerekiyor — switch tek başına yetmiyor.

```
192.168.1.1 (Muhasebe PC)  ─┐
192.168.1.2 (Muhasebe PC)  ─┤── Switch ── (aynı ağ, direkt konuşur)
192.168.1.3 (Muhasebe PC)  ─┘
```

```
192.168.2.1 (IT PC) ─┐
192.168.2.2 (IT PC) ─┤── Switch ── Router ── (farklı ağ, router gerekli)
```

### VLAN nedir?
VLAN, VXLAN vb. terimlerin/çözümlerin/yöntemlerin/tekniklerin neye istinaden geliştirildiğini/ortaya çıkarıldığını anlayabilmek için önce bu tip çözümlemelerin ortaya çıkmadan önce ki meydanda olan mevcut halin/sorunların anlaşılması gerekli. Böylece bu çözümler öğrenilmek istenen konu kapsamında daha iyi kavranacaktır. Konuyu doğrudan ortaya çıkmış bir çözüm üzerinden anlamaya çabalamak kafa da çok fazla boşluğun kalmasına sebebiyet verebilir. Örneğin bir ağ mevcut (tüm uç cihazların bir switch'e bağlı olduğu bir topoloji) ve bu ağ segmentlendirilmek/bölümlendirilmek isteniyor. Çünkü aynı ağ içerisinde ki bazı uç cihazların bir diğer başka uç cihazlar ile iletişim kurmasına gerek olunmadığına karar verildi. Veya güvenlik için bölümlendirme yapılmak istendi. Veya tamamen bölümlendirilme yapılmak istendiğinden bu yapılmak isteniyor (tamamen keyfi). ağın bazı cihazları muhasebe bazı cihazları IT bölümünde/segment'inde olacak şekilde dilimlenmesi gerek. Ancak switch'in malum niteliği sebebiyle (iletim için tek bir broadcast domain olması) birbirlerinden izole bölümlendirilme yapılamıyor. Bunun için Layer 2 katmanında yani switch gibi cihazların anlayabileceği VLAN adlı bir çözüm devreye sokulabilir oluyor. Switch'e _"bu portlar Muhasebe VLAN'ı, şu portlar IT VLAN'ı, birbirlerini göremezler"_ diyebiliyorsun. VLAN switch'e Layer 3 farkındalığı kazandırmadan mantıksal segmentleme özelliği kazandırıyor. VLAN'ın getirdiği çözüm şu; normal de switch'e bağlı cihazlar tek bir broadcast domain üzerinden birbirleriyle haberleşiyor ancak yukarıda ki örnekte de belirtildiği üzere muhasebe ve IT departmanları birbirleriyle hiçbir zaman iletişim kurmayacaksa (veya genellikle) o halde bu broadcast domain'i her iletim esnasında meşgul etmenin bir yararı yok (çünkü örneğin muhasebe departmanında ARP request atıldığında gereksiz yere IT departmanında ki cihazada bu paket gidecek). Bunun yerine birden fazla broadcast domain'i olsun her biri kendi segment'i ile ilgilensin/yayın yapsın. VLAN, Layer 2 seviyesinde ağı mantıksal olarak bölerek ayrı broadcast domain’ler oluşturur. VLAN şu problemleri çözer:

-  Broadcast trafiğini azaltır:
Tek ağ → herkes ARP alır
VLAN → sadece kendi grubun görür

-  Güvenlik sağlar
Aynı switch üzerinde izolasyon
Örn:
Muhasebe VLAN 10
IT VLAN 20

- Fiziksel değil mantıksal ayrım
Aynı kablo, aynı switch
Ama sanki ayrı network gibi davranır

VLAN, fiziksel olarak aynı switch üzerinde bulunan cihazları, Layer 2 seviyesinde ayrı ağlar (broadcast domain’ler) haline getirir. Bu ağlar genellikle farklı IP subnet’leri ile eşleştirilir ama bu zorunlu değildir.

| VLAN    | Subnet             |
| ------- | ------------------ |
| VLAN 10 | 192.168.1.0/24     |
| VLAN 20 | **192.168.1.0/24** |
Yani Aynı IP bloğu Ama farklı VLAN →  iletişim yok Neden? Broadcast domain ayrı ve ARP birbirine ulaşamaz veya;

| VLAN    | Subnet             |
| ------- | ------------------ |
| VLAN 10 | 192.168.1.0/24     |
| VLAN 20 | **192.168.2.0/24** |

Her VLAN = ayrı subnet. Aralarında iletişim için router gerekir. İki dizayn/tasarım da çalışır.

### Layer 3 cihazları ile mantıksal olarak ağ segmenlendirilmesine rağmen neden Layer 2 katmanında bu sorun çözülmeye çalışılmıştır?
Küçük topolojilerde VLAN kullanmadan izolasyon ve segmentleme yapılmak isteniyorsa Layer 3 katmanında çalışan cihazlar kullanılabilir. Bu bir tasarım mevzusudur. İstenirse küçük topolojilerde VLAN'da kullanılabilir ancak sorun büyük topolojilerde ortaya çıkıyor. Örneğin bir veri merkezinde binlerce sunucu var. Her sunucu arası iletişim için router kullansaydık ne olurdu? Router her paketi işlemek zorunda. Çok yavaş ve pahalı olurdu (geçmişte router'lar pahalıydı). Ağ trafiği sürekli Layer 3’e çıkıp geri inerdi. Bu ciddi bir performans kaybı. Switch’ler ise donanımsal (ASIC) çalışır çok daha hızlı frame iletir. Ayrıca ucuz. Büyük hacimli trafiği kolayca taşıyor. Bu yüzden aynı ağ içindeki iletişim için switch, farklı ağlar arası için router kullanılıyor. VLAN ile aynı fiziksel switch üzerinde, donanım hızında birden fazla mantıksal ağ oluşturabiliyorsun. amaç segmentasyonu Layer 3’e bırakmadan, Layer 2 seviyesinde daha hızlı ve esnek yapmak. VLAN’ın getirdiği kritik avantaj sayesinde switch kendi içinde: VLAN 10 → ayrı ağ, VLAN 20 → ayrı ağ segmentasyonu yapar. Trafik switch içinde kalır (wire speed). Router sadece gerektiğinde devreye girer. Bu da Router’a aşırı yük gereksiz hop yaptırmaz. Ölçeklenebilirlik problemi oluşturmaz. Ayrıca bu aslında _“ya VLAN ya router”_ mevzusu da değil. Bir ağ topolojisinde de zaten switch ve router birlikte de kullanılabilir: 

Router / Layer 3 switch → VLAN’lar arası iletişim:

```
VLAN 10 (Muhasebe) --- Router --- VLAN 20 (IT). 
```

Buna **Inter-VLAN Routing** denir.

Eğer VLAN yoksa tüm cihazlar aynı broadcast domain'i kullanır bu da paket iletiminin gerçekleştirilmesi için aynı ağda ki tüm cihazları etkilediğinden ağı yorar. Yükü hafifletmek için ayrım yapılması gereklidir bu da ya fiziksel olarak ayırmak anlamına gelir (maliyetli, aşırı teçhizat) ya da tüm trafiği router’a zorlamak anlamına gelir (pahalı ve performans kaybı). Ancak VLAN ile farklı VLAN bölümleri oluşturulur bu da her bir VLAN bölümüne özgü brodcast domain anlamına gelir ve böylece bir iletim durumunda iletim, yalnızca kendisini ilgilendiren VLAN alanına sorgu/yayın/iletim yapar.
### VLAN egzersizi

```
PC-1 ─┐
PC-2 ─┤── Ethernet Switch
PC-3 ─┘
```

Cihazlarin IP'leri atanmış ve birbirlerine `ping` atilabilir şekilde ayarlanmış olan bu topolojiyi kurun. GNS3'te _"ethernet switch"_ cihazina çift tıklanıldığında _"Ports"_ bölümü var. Bu bölüm switch cihazinda ki port'lara özgü yapılandırmaların yapılabileceği bir liste ekranıdır. `PC-1`'i `port 0`'a, `PC-2`'yi `port 1`'e ve `PC-3`'ü de `port-2`'ye bağladığımızı düşünelim. Bu örnekte `PC-1` ile `PC-2`'yi `VLAN 1`'e `PC-3`'u de `VLAN 2`'ye ayarlayacağımızı düşünelim. Amaç `PC-3`'ün diğer cihazlara `ping` atamamasını sağlamak yani diğer cihazlardan izole etmektir. _"Ports"_ bölümünde `PC-3`'e bağlı olan port'a çift tıklayin. _"Settings"_ bölümünde bunun ile ilgili ayarlar gözükecektir. `PC-3` `VLAN 1`'de olduğundan _"VLAN"_'ı ayarlama kısmından bunu `2` olarak değiştirin ve _"Add"_ deyin. Ardından bu ayarları uygulayın. `PC-1`'den veya `PC-2`'den `PC-3`'e `ping` atmaya çalışıldığında bu cihazlar aynı subnet'de olmasina rağmen paketlerin gitmediği gözlemlenebilir olacaktır. Ayrıca `PC-1/2`'in terminalinden `arp -n` komutu ile ARP tablosunda `PC-3`'ün MAC adresinin görüntülenemediği gözlemlenebilir yani VLAN'ın başarıyla uygulandığı bu şekilde doğrulanabilir. Veya `PC-3` ile Switch arası bağlantı Wireshark ile incelenecek olursa ve `PC-1` veya `PC-2`'ye `ping` atılacak olursa bunun iletilemediği gözlemlenebilir.

### Gerçek senaryo da VLAN ağ dilimlemesi teknik olarak nerede ve nasıl yapıyor? Ayrım tam olarak nerede yapılıyor konfigüre ediliyor?

VLAN ile ağ izolasyonu ve bölümlendirilmesi, ilgili cihaz da yani **switch'te** yapılır. Switch, port'larına bağlı cihazları VLAN tekniği sayesinde ayırabilir. Bunun için switch'in terminal arayüzüne erişilmesi gereklidir. Bu da klasik olarak (tıpkı bir ev router'ını konfigüre eder gibi) bir PC'yi switch'e kablo ile bağlayıp PC terminalinden switch'in terminal arayüzüne erişilerek yapılır. Erişim yapıldıktan sonra orada bulunan araçlar ile switch üzerinde ki port'lara VLAN ID tag'lemesi (etiketlemesi VLAN 10, VLAN 20 vb. gibi) yapılır. Böylece switch yapılan konfigürasyona göre hangi portunun VLAN ID etiketlemesi yapıldığını bilir. Yani o port'a bağlı olan cihaz VLAN 10’dadır **değil**, bu switch portu VLAN 10’dadır (yani bu port'a bağlı olan cihaz dolaylı olarak VLAN 10'da olmuş oluyor). İzolasyonun veya ayrımın bilgisi yalnızca switch tarafından bilinir yani sadece kendi kendine bu ayrım bilgisine sahiptir. Ağın paket iletimi ve kontrollerinin hepsi onun üzerinden geçtiğinden yapılan konfigürasyona göre kendince ağ dilimlendirmesi ve izolasyon yönetimini böyle yapabilir.

```
PC-1 ─ Port 1 ┐
PC-2 ─ Port 2 ┤ ── Switch
PC-3 ─ Port 3 ┘
```

Switch’e diyorsun ki:
```
Port 1 → VLAN 10
Port 2 → VLAN 10
Port 3 → VLAN 20
```

Sonuç olarak;

```
PC1 ve PC2 → aynı VLAN’da
PC3 → farklı VLAN’da
```

Switch aslında şunu yapıyor;

MAC + Port + VLAN tablosu;

```
MAC A → Port 1 → VLAN 10
MAC B → Port 2 → VLAN 10
MAC C → Port 3 → VLAN 20
```

Bu şekilde switch izolasyonu şu kuralı uygulayarak mümkun kılar; _“Aynı VLAN içindeki portlar birbirini görür, farklı VLAN’lar görmez”_;

```
Port 1 (VLAN 10) → Port 2’ye gönderilebilir
Port 1 (VLAN 10) → Port 3’e gönderilemez
```

Switch bunu nasıl biliyor? Switch’in içinde **VLAN database + forwarding logic** vardır yani;

1. Paket gelir
2. VLAN tag veya port bilgisi okunur
3. Lookup yapılır
4. Sadece o VLAN içinde forward edilir

Switch kendisine bağlı olan cihazdan bir paket aldiginda o port'un VLAN ID'si zaten ayarlı ve konfigüreli oldugundan paketi tag'leyebilir (etiketler). Etiketliyebilir olmasının sebebi ağın yapısına göre değiştiğinden switch'in davranışını da değiştirebilir bu yüzden bununla ilgili iki yöntem vardır;

1. Access port (PC’ye bağlı)
- VLAN tag YOK
- Switch içeride ekler/siler

```
PC ─── (access port) ─── Switch
```

PC, VLAN'ı bilemeyeceğinden (IP Layer 3 katmanında çalıştığından) switch'e sadece normal Ethernet frame gönderir;

```
| MAC | MAC | Data | -> gibi
```

 Paket Switch’e gelince switch şunu yapar. Paketin hangi porttan geldiğini bilir ve o port _“VLAN 10 access port”_ diye ayarlıdır paketi VLAN 10’a ait kabul eder eğer paket switch’ten çıkacaksa başka switch’e giderken tag eklenebilir. Özetle VLAN bilgisi çoğu zaman porttan türetilir.

2. Trunk port (switch-switch arası)
- VLAN tag VAR
- Switch tag’i korur

```
Switch A ─── trunk ─── Switch B
```
Burada ise VLAN tag taşınır - switch tag eklemez veya silmez (çoğu durumda). Yani _Switch A_ tag eklemiş olabilir. _Switch B_ aynen kabul eder.

VLAN pakete ne yapar? Normal bir Ethernet frame:

```
| MAC Dest | MAC Src | Type | Data | CRC |
```

VLAN eklenince araya küçük bir etiket girer:

```
| MAC Dest | MAC Src | VLAN TAG | Type | Data | CRC |
```

Bu etiket VLAN ID (örneğin 10, 20). Bu yapının sebebi: IEEE 802.1Q ile ilgilidir. Özetle VLAN bir _“paket özelliği”_ değil switch’in pakete eklediği “etiket”'dir.

### VLAN'ın teknik sınırları ve yetersizliği
VLAN ile bir subnet'i dilimlendirme belirli sayıya kadar gerçekleştirilebilir. Bu tekniğin tasarımı gereği yani VLAN ID'si **12 bit** ile temsil ediliyor yani  yani `2¹² = 4096`, bunun 2'si özel ayrılmış, geriye **4094** kullanılabilir ID kalıyor. Bu teknik bir sınır. VLAN standardı (802.1Q) tasarlanırken 4094'ün yeterli olacağı düşünülmüş. Ama internet ve bulut bilişim büyüyünce bu sayı yetersiz kaldı. Yani bir veri merkezinde VLAN tekniği ile ağ bölümlendirmesi yapmak mümkün ancak daha fazlası gerektiğinde bu gerçekleştirilemiyor. Bunun çözümü içinse VXLAN geliştirilmiştir. Ayrıca bu yeni teknik ile sadece daha fazla sanal ağ ID'si arttırmakla kalmamış aynı zaman da farklı çözümleri de beraberinde getirmiştir.

Bu tekniğin veri merkezlerinde kullanılacağı düşünülürse ve mevcut ağın dilimlenip neden izolasyon yapılmak istendiği üzerine düşünülürse ve buna müteakip çok kabaca bir örnek verilecek olursa; bir clous sağlayıcısı düşünelim ve basit bir yapılı ağına tek bir VLAN uygulanmış olsun. Bu sağlayıcı, ağına tek bir VLAN uyguladığı icin 4096 adet müşteriye kendi ağ altyapısı üzerinde VPC hizmeti verebilir (her müşterinin yalnızca tek bir VPC hizmetinden yararlanabileceği düşünülürse). Ancak bir fazlasını yani 4097. müşteriye VPC yani kendi altyapısı üzerinde özel ağ kurma hizmeti sağlayamazdı. İşte bu soruna çözüm olarak VXLAN ortaya çıkmış ve ağı **2 üzeri 24 adet yani 16.7 milyon** dilime bölümlendirebilir hale getirmiştir. Bu da yine konunun anlaşılması açısından kabaca ifade edilecek olursa 16.7 milyon tane müşteri demektir. Tabii gerçek senaryolarda bir müşteri istediği kadar da VPC hizmeti kullanabilir ve cloud sağlayıcıları merkezlerini donanımsal açıdan daha fazla geliştirip daha fazla VXLAN yapılı ağlar kurup daha fazla ağ dilimlemesi elde edebilirler ki sistem zaten kabaca bu yapının üzerinde işliyor.

### VXLAN nedir?

VLAN'in sanal ağ ID sayısı tasarımı gereği büyük veri merkezleri gibi yerlerde yetersiz kalmasından ötürü bunun üstüne geliştirilen VXLAN yalnızca sanal ağ ID sayı aralığını fazlalaştırmak ile kalmamış aynı zaman da farklı fiziksel lokasyonlarda bulunan ağları sanki aynı switch'e bağlılarmış gibi zannettirme davranışını da sergilemesi sağlanmıştır. Yani İstanbul'daki sunucu ile Ankara'daki sunucu aralarında internet olmasına rağmen sanki aynı switch'e bağlıymış gibi davranabilir. Buna **Overlay network** deniyor mevcut ağın üzerine sanal bir Layer 2 ağı örüyorsun (tünelleme).

```
VLAN'ın sorunu → Tek bir fiziksel lokasyona sıkışık,
                  İstanbul'daki VLAN Ankara'ya uzanamıyor
VXLAN'ın çözümü → İnternet üzerinden tünel açarak
                   uzak lokasyonları aynı Layer 2 ağda birleştiriyor
```

| Özellik | VLAN          | VXLAN              |
| ------- | ------------- | ------------------ |
| Değişim | Tag ekler     | Paket kapsüller    |
| Katman  | Layer 2       | Layer 3 üstü       |
| Kapsam  | Local network | Datacenter/Cloud   |
| Cihaz   | Switch        | VTEP (host/router) |
| Amaç    | Ayrım         | Taşıma + ölçek     |

### VLAN ile VXLAN'ın konfigürasyonel farklılıkları

VLAN'ı ağ da uygulamak için switch üzerinde bir konfigürasyon yapılıyordu. Bunun sebebi bütün ağın paket iletimi switch cihazı üzerinden sağlanmasından ötürü ağ izolasyonu/dilimlemesi/bölümlendirmesi bu cihazın terminal arayüzünden veya varsa grafik arayüzüne erişilip gerekli ayarın ayarlanmasıyla mümkün kılınıyordu (port bazlı bir ayar). Ancak VXLAN farklı, switch üzerinde değil, **VTEP** cihazları üzerinde yapılıyor. VXLAN'da konfigürasyon VTEP uygulanabilir bir cihaz üzerinden sağlanıyor. _"VTEP = VXLAN Tunnel Endpoint"_ tüneli açan ve kapatan cihaz. Yani proje de FRR yüklü olan custom docker router'larımız VTEP cihazı olarak ayarlanabiliyor/formlandırılabiliyor.

VTEP şunu yapıyor:

```
Host-1'den paket geliyor (end device)
        ↓
VTEP-1 paketi alıyor (FRR router)
        ↓
Üzerine VXLAN başlığı ekliyor (encapsulation)
        ↓
Normal IP paketi gibi internetten gönderiyor
        ↓
VTEP-2 paketi alıyor (other FRR router)
        ↓
VXLAN başlığını soyuyor (decapsulation)
        ↓
Host-2'ye iletiyor (other end device)
```

### VXLAN'ın İşleyişi
VXLAN'ın yaptığı işlem özetle kendisine gönderilen Layer 2 paketini Layer 3 paketi olarak sarmalamak.

```
İç paket (Layer 2) → MAC adresleri, ethernet frame
Dış paket (Layer 3) → IP adresleri, normal internet paketi
```

Yani VTEP cihazı (FRR router'ımız) şunu yapıyor:

- Host-1'den gelen Layer 2 ethernet frame'ini alıyor
- Onu bir UDP paketi içine koyuyor
- Bu UDP paketi normal internet üzerinden gidiyor
- Karşı taraftaki VTEP UDP paketini açıyor
- İçindeki Layer 2 frame'i çıkarıp Host-2'ye iletiyor

Host-1 ve Host-2 hiç farkında değil onlar için sanki aynı switch'e bağlılar. Aradaki tüm Layer 3 işlemi onlardan gizli. Yani VXLAN Layer 2'yi taklit ediyor ancak gerçekte Layer 3 üzerinden taşıyor ama uç cihazlara Layer 2 gibi görünüyor. Daha detaylı olarak düşünecek olursak uç cihazdan gelen paketin Layer 2 frame'ini Layer 3 olarak kılıflandırıyor;

```
Host-1'den gelen ethernet frame (Layer 2)
        ↓
VTEP bu frame'i olduğu gibi alıyor
        ↓
Üzerine VXLAN başlığı + UDP + IP sarıyor
        ↓
Artık normal bir internet paketi gibi görünüyor
        ↓
Karşı VTEP bu paketi açıyor
        ↓
İçindeki orijinal Layer 2 frame çıkıyor
        ↓
Host-2'ye iletiyor
```

### Uç cihazlar Layer 3 katmanında çalışan cihazlar ise nasıl Layer 2 paketi gönderebiliyorlar?
Bir web sitesine istek atıldığında bilgisayar ne gönderiyor? Sadece IP paketi mi? Hayır. Her cihaz bilgisayar, telefon, sunucu ağa bir şey gönderirken her zaman hem Layer 2 hem Layer 3 kullanıyor. Katmanlar iç içe:

```
Uygulama verisi
      ↓
Layer 3 (IP başlığı ekleniyor)
      ↓
Layer 2 (MAC başlığı ekleniyor → ethernet frame)
      ↓
Fiziksel kablo
```

Yani her cihaz veriyi göndermeden önce katman katman sarıyor. Karşı taraf da katman katman açıyor. _"Layer 3 cihazı"_ veya _"Layer 2 cihazı"_ derken aslında o cihazın hangi katmana kadar baktığını kastediyoruz:

```
Switch → Layer 2'ye kadar bakıyor, MAC adresine göre yönlendiriyor
Router → Layer 3'e kadar bakıyor, IP adresine göre yönlendiriyor
Host → tüm katmanları kullanıyor
```

Yani host cihazlar da Layer 2 paketi gönderiyor. Her zaman. VXLAN VTEP bu Layer 2 paketini yakalayıp kılıf olarak kullanacağı Layer 3 paketinin içine koyuyor.

### Statik mod ile temel ve basit bir VXLAN topoloji örneği

```
Host-1 ── Router-1 ══VXLAN tüneli══ Router-2 ── Host-2
```

**Router-1** ve **Router-2** VTEP görevi yapacak. İlk olarak statik mod ile başlayacağız yani VTEP'lerin birbirinin IP'sini elle gireceğiz.

Topoloji IP planı:
```
Host-1 tarafı → 192.168.1.0/24
Router'lar arası → 10.0.0.0/30
Host-2 tarafı → 192.168.2.0/24
```

IP planı uygulandıktan ve `ping` ile iletişimin sağlandığı doğrulandıktan sonra _"Underlay"_ ağın çalıştığıyla/kurulu olduğuyla ilgili hemfikir olunabilir. VXLAN bağlamında bu fiziksel ağa _"Underlay"_ deniyor. Şimdi ise _"Overlay"_ yani VXLAN ile sanal ağ yapılandırılması için VXLAN tünelini kuracağız. Router-1'in terminalinde şu komutu çalıştır:

```
ip link add vxlan10 type vxlan id 10 remote 10.0.0.2 local 10.0.0.1 dev eth1
```

Bu komut satırı kısım kısım incelenecek olursa;

- `ip link` -> komutunun genel kullanımı: ağ arayüzlerini yönetmek — oluşturmak, silmek, aktive/deaktive etmek. Daha önce `ip link set eth0 up` ile aktive etmiştik, şimdi ise `ip link add` ile yeni bir sanal arayüz oluşturuyoruz. Kısaca ağ arayüzleri ile ilgili ayarlar yapmayı sağlayan komut aracı.
- `ip link add vxlan10` -> ismi `vxlan10` olacak şekilde yeni bir ağ arayüzü oluşturuyoruz.
- `type vxlan id 10` -> bu ağ arayüzünün tipinin `vxlan` bir sanal ağ olacağını ve id numarasının ise `10` olacağı belirtiliyor.
- `remote 10.0.0.2` -> bu kısım ise karşı VTEP cihazımızın IP adresini belirttiğimiz kısım (statik mod kısmı burası yani manuel olarak karşı VTEP cihazının IP adresini elle girdiğimiz bölüm)
- `local 10.0.0.1` -> bu şuan da ayarı yapılan VTEP cihazının kendi IP adresi. Yani _"ben kimim?"_ sorusunun cevabı. VXLAN paketi gönderirken kaynak IP olarak bu kullanılacak.
- `dev eth1` -> bu tünelin hangi fiziksel arayüz üzerinden çalışacağı. Router-1'in Router-2'ye bağlı arayüzü `eth1`. Tünel trafiği buradan akacak.

Özetle:

```
"vxlan10 adında bir VXLAN arayüzü oluştur,
VNI ID'si 10 olsun,
karşı VTEP 10.0.0.2'de,
ben 10.0.0.1'im,
eth1 arayüzünü kullan"
```

komut çalıştırıldığı taktirde bir uyarı mesajı çıktısı verebilir şunun gibi;

```
vxlan: destination port not specified
Will use Linux kernel default (non-standard value)
Use 'dstport 4789' to get the IANA assigned value
Use 'dstport 0' to get default and quiet this message
```

Bu bir hata değil uyarı mesajıdır `ip a` komutu ile ağ arayüzleri listesine bakılacak olursa `vxlan10` isimli sanal ağ arayüzünün oluşturulduğu görülebilir. Bu uyarı ne diyor? _"VXLAN için hangi port numarasını kullanacağımı belirtmedin. Linux'un kendi varsayılan değerini kullanacağım ama bu IANA'nın belirlediği standart değil."_ IANA = Internet Assigned Numbers Authority port numaralarını standartlaştıran kurum. VXLAN için resmi port _**4789**_. Yapmadan olur muydu? Teknik olarak çalışırdı ama iki VTEP cihazı farklı portlar kullanırsa birbirini anlayamaz. _**4789**_ yazarak _"ikimiz de aynı standart portu kullanalım"_ demiş oluyoruz. Ayrıca VXLAN bir protokol ve bu protokol UDP üzerinden çalışıyor. UDP paketleri gönderilirken bir port numarası belirtmek zorunda. Router-2 bir UDP paketi aldığında _"bu paket kime?"_ diye soruyor. Pakette port numarası var ve _"4789 portuna gel"_ diyor. Router-2 _**"4789"**_ portunu dinleyen VXLAN servisine paketi iletiyor. Burada servisten kastedilmek istenen tam olarak şu; Linux arka planda _"4789 portuna gelen UDP paketlerini ben karşılarım"_ diyor. Bu VXLAN'ın kernel içinde ki işleyişi. Eğer port belirtmezsen:

- Router-1 bir port kullanıyor
- Router-2 başka bir port bekliyor
- Paketler eşleşemiyor

Standart port 4789 olduğundan ikisi de aynı portu kullanıyor ve iletişim kuruluyor.
Kısaca VXLAN bir servis değil ama UDP üzerinden çalıştığı için port numarası şart ve 4789 herkesin anlaştığı standart port.

```
80  → HTTP (web)
443 → HTTPS (güvenli web)
22  → SSH
4789 → VXLAN (IANA standardı)
```

gibi düşünülebilir.

komut uygulandiysa şu komut ile ağ arayüzünü silip;
```
ip link delete vxlan10
```

port'un `4789` olarak ayarlandığı şekliyle yeniden ağ arayüzünü oluşturun;
```
ip link add vxlan10 type vxlan id 10 remote 10.0.0.2 local 10.0.0.1 dstport 4789 dev eth1
```

ardından arayüzü aktive et;
```
ip link set vxlan10 up
```

Sonra Router-2'de de aynı işlemi yap ama dikkat, local ve remote IP'leri yer değiştirecek:
```
ip link add vxlan10 type vxlan id 10 remote 10.0.0.1 local 10.0.0.2 dstport 4789 dev eth1
ip link set vxlan10 up
```

Şimdi bridge'i kuracağız. Bridge, host'tan (end devices) gelen trafiği VXLAN tüneline aktaran sanal bir switch gibi düşünülebilir. Bridge burada VTEP cihazina bağlı olan end device'ların trafiğini fizikselden (underlay) değilde VXLAN trafiğinden yani tünelinden (overlay) geçirmek için konfigüre edilmesi gereken bir ayardır.

```
Host-1 (eth0) → Bridge (br0) → vxlan10 arayüzü → tünel
```

Bridge, host'un ethernet trafiğini VXLAN tüneliyle buluşturuyor. Yani host normal ethernet paketi gönderiyor, bridge onu VXLAN'a yönlendiriyor. Host'un VXLAN'dan haberi yok. Host tamamen habersiz, sadece normal ethernet paketi gönderiyor. VTEP (router) her şeyi hallediyor. Host'un ilgilendiği tek şey paketin gönderilip gönderilemeyeceğidir. Tabii ki biz arkaplanda paketin gönderilebilmesi için arkaplan ayarları (overlay konfigürasyonları) yaptığımızdan paket gönderilecektir. Bunun mümkün kılanabilmesi için Router-1'de şu komutların uygulanması gerekli;

```
ip link add br0 type bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth0 master br0
```

her bir komutu teker teker ele alacak olursak;

- ilk komut `bridge` tipinde ve `br0` isminde bir köprü ağ arayüzü oluşturuyor.
- ikinci komutta bunu aktive ediyoruz.
- `ip link set vxlan10 master br0` --> `vxlan10` arayüzünü `br0` bridge'ine bağla
- `ip link set eth0 master br0` --> `eth0` arayüzünü `br0` bridge'ine bağla

`master` keyword'ü şunu demek: _"bu arayüzün sahibi br0 olsun."_ Yani `br0` bir switch gibi davranıyor ve hem `eth0` hem `vxlan10` onun portları oluyor. Veya bir boru veya köprü gibi düşünülürse bunların iki ucunun nereye bağlanması gerektiğinin belirtimi yapılıyor gibi düşünülebilir yani akacak trafiğin her iki ucunun nerelere bağlanması gerektiği gibi.

```
Host-1 → eth0 → br0 → vxlan10 → tünel → Router-2
```

`br0` ortada duruyor ve ikisini birleştiriyor. host'tan gelen trafik VXLAN tüneline, tünelden gelen trafik host'a akıyor. Şimdi Router-2'de de aynı komutları çalıştır;

```
ip link add br0 type bridge
ip link set br0 up
ip link set vxlan10 master br0
ip link set eth0 master br0
```

bridge yapılandırması da yapıldıktan sonra son olarak her iki cihazın aynı subnet aralağında olması sağlanarak sanki aynı local ağda veya switch'e bağlılarmış zannını vereceğiz bunun için;

Host-1'in `eth0` ağ arayüzüne IP ata:

```
ip addr add 30.1.1.1/24 dev eth0
```

Host-2'ye de:
```
ip addr add 30.1.1.2/24 dev eth0
```

Kurgumuz her iki cihazda da `eth0` ağ arayüzünde aynı subnet'e sahip cihazların birbirlerine uzak lokasyonlarda dahi olsalar (yani aralarında internet dahi olsa) sanki aynı switch'e veya aynı lokasyondalarmış davranışını zannettirmek veya sergiletmek olduğundan her iki cihazin aynı subnet'de olduğu IP adresleri atanmalıdır. Bu şekilde arkaplanda ki VXLAN mimarisi çalışacaktır. Ve bu IP adresleri atandığı anda artık **"Overlay"** bir network'e sahip olunuyor. Underlay ağımızda zaten `192.168.1.0/24` ve `192.168.2.0/24` subnet'leri var. VXLAN tüneli üzerindeki sanal ağ tamamen ayrı bir ağ farklı bir subnet kullanarak _"bu IP'ler VXLAN üzerinden geliyor"_ diyebiliyoruz. Host-1 `(30.1.1.1)` ve Host-2 `(30.1.1.2)` aynı subnet'de `30.1.1.0/24`. Aralarında router yok, sanki aynı switch'e bağlıymış gibi. VXLAN bunu sağlıyor. Host-1'den Host-2'ye `ping` atarak "Overlay" ağın çalışıp çalışmadığı test edilebilir;

```
ping 30.1.1.2
```

Özet olarak;

- Host-1 `192.168.1.0/24` ağında
- Host-2 `192.168.2.0/24` ağında
- Ama ikisi de `30.1.1.0/24` overlay ağında birbirini görüyor

Sanki aynı switch'e bağlıymış gibi. Router'lar arası gerçek ağdan tamamen habersizler. Durumu daha da analiz etmek icin Router-1 ile Router-2 arasında ki kabloya Wireshark aç ve ping at. Wireshark'da herhangi bir frame'in (şayet paketler hedefe iletiliyor ise) içeriği incelenecek olursa paketin bir kapsül paket olduğu saptanabilir. VNI degeri, VXLAN oldugu, kaynağın aslında `10.0.0.1`'den `10.0.0.2`'ye olduğu vb. gibi detaylar Wireshark aracıyla teyit edilebilir.

### Unicast, Multicast, Broadcast nedir?
Şu biçim de benzerlik kurarak anlatmak gerekirse; bir sınıfta öğretmen olduğunu düşün:

**Unicast** → Tek bir öğrenciye konuşmak. _"Ahmet, tahtaya gel."_ Sadece Ahmet duyuyor, mesaj tek hedefe gidiyor.
**Broadcast** → Tüm sınıfa bağırmak. _"Herkes defterini çıkarsın!"_ Sınıftaki herkes duyuyor, kaçış yok.
**Multicast** → Belirli bir gruba konuşmak. _"Matematik kulübü üyeleri yarın toplanıyor."_ Sadece o kulübe kayıtlı olanlar ilgileniyor, diğerleri görmezden geliyor.

Ağ da karşılıkları:

```
Unicast   → tek bir IP'ye paket gönder (192.168.1.1)
Broadcast → ağdaki herkese gönder (192.168.1.255)
Multicast → belirli bir gruba gönder (224.0.0.5 gibi özel adresler)
```

OSPF'te Hello paketleri `224.0.0.5` adresine gidiyordu. Bu bir **multicast adresi.** Sadece OSPF çalıştıran router'lar bu adresi dinliyor. VXLAN multicast modunda da benzer şekilde VTEP'ler bir multicast grubuna üye oluyor ve birbirlerini bu şekilde keşfediyor.

### Unicast, Multicast ve Broadcast bunlar cihaz tarafından arkaplanda otomatik olarak gerceklestirilen mekanikler. Örneğin bir cihazin unicast veya multicast olarak davranması gerektiği nasıl belirtiliyor?

**Unicast** → Hedef IP tek bir cihazın IP'si olduğunda otomatik unicast oluyor. Örneğin `ping 192.168.1.1` — bu unicast, ayrıca belirtmene gerek yok.
**Broadcast** → Hedef IP subnet'in broadcast adresi olduğunda otomatik broadcast (ARP oldugunda kullanilir). Örneğin `192.168.1.255` — bu broadcast, otomatik.
**Multicast** → Hedef IP `224.0.0.0/4` aralığında olduğunda multicast. Yani `224.x.x.x` ile `239.x.x.x` arası IP'ler multicast için ayrılmış özel adresler. Yani aslında hedef IP adresi hangi davranışın olacağını belirliyor:

```
Hedef IP = tek cihaz IP'si    → unicast (otomatik)
Hedef IP = 192.168.1.255      → broadcast (otomatik)
Hedef IP = 224.x.x.x          → multicast (otomatik)
```

VXLAN multicast modunda da şunu yapıyoruz: VTEP'e _"`239.1.1.1` multicast grubunu dinle"_ diyoruz.

### `224.x.x.x` ile `239.x.x.x` arası multicasting yapabilmek için özel olarak ayrılmış IP adresleri
IP adres aralıkları aslında belirli amaçlar için ayrılmış. IP adres uzayı IANA tarafından bölünmüş tıpkı bir şehirde farklı bölgelerin farklı amaçlar için ayrılması gibi.

Önemli özel aralıklar:

```
10.0.0.0/8        → özel ağlar (ev, şirket)
172.16.0.0/12     → özel ağlar
192.168.0.0/16    → özel ağlar (en yaygın ev ağı)
127.0.0.0/8       → loopback (kendine ping)
224.0.0.0/4       → multicast
```

Multicast aralığı `224.0.0.0` - `239.255.255.255` bu aralıkta ki IP'ler hiçbir zaman tek bir cihaza atanmıyor. Sadece grup iletişimi için kullanılıyor. Bu aralık da kendi içinde bölünmüş:

```
224.0.0.0/24    → yerel ağ multicast (OSPF, STP gibi protokoller)
224.0.0.5       → OSPF router'ları
224.0.0.6       → OSPF designated router'lar
239.0.0.0/8     → yerel kullanım için ayrılmış (VXLAN gibi)
```

`239.x.x.x` aralığı özellikle _"sen kendin kullanabilirsin"_ diye ayrılmış. VXLAN multicast grubu için buradan bir adres seçiyoruz.
### Broadcast ve ARP ilişkisi nedir? Bir cihaz ne zaman ARP atar? ARP her zaman mı atılır yoksa gerektiğinde mi? Gerektiği zaman ne zaman?
Basit bir ifade ile bir makine bir diğer makineye paket göndereceği zaman hedefi aynı subnet içerisinde ki bir IP ise bu cihazın MAC adresini öğrenebilmek için tüm ağa bu IP'ye sahip makinenin MAC adresini sorar ve ağda ki cihazlar bu IP'ye sahip degilse (yani bu IP ile esleşmez ise) MAC adresi alamaz. Yalnızca bu IP ile eşleşen cihaz _"işte bu benim ve MAC adresim budur."_ MAC adresini istek atan makineye cevap olarak geri iletir. Yani bu şekilde ARP yalnızca aynı subnet'te atılır. Bunu da broadcast aracılığıyla mümkün kılar.

1. **Trafik Tipleri: Kim, Kime Gönderiyor?**
Bu üç kavram, verinin ağdaki **hedef kitlesini** belirler.

| Tip           | Hedef                           | Örnek                                                                      |
| :------------ | :------------------------------ | :------------------------------------------------------------------------- |
| **Unicast**   | Birebir (One-to-One)            | Sen Google’a bir paket gönderdiğinde sadece o sunucuya gider.              |
| **Broadcast** | Herkese (One-to-All)            | Bir cihaz _"Benim IP'm bu, burada kimler var?"_ dediğinde tüm ağa bağırır. |
| **Multicast** | Belirli bir gruba (One-to-Many) | Bir video konferans yayınında sadece o yayına katılanlara veri gider.      |
2. **ARP (Address Resolution Protocol) Nedir?**
Cihazlar birbirleriyle IP adresi üzerinden konuşmak isterler ama yerel ağda (Ethernet seviyesinde) iletişim kurmak için birbirlerinin **MAC adreslerine** ihtiyaç duyarlar. Cihaz bir IP'ye ulaşmak istediğinde o IP'nin kime ait olduğunu (MAC adresini) bilmiyorsa **Broadcast** yapar. Bu _"Bağırarak sorma"_ işlemine **ARP Request** denir. Bağırarak sorma benzetmesinin sebebi tüm ağa bu isteği duyurması yüzündendir.

3. **Cihaz Ne Zaman ARP Atar?**
Cihazın her saniye _"başıboş"_ şekilde ARP atmaz. ARP'nin tetiklendiği durumlar şunlardır:

* **İlk İletişim:** Bir IP'ye ilk kez paket göndereceğin zaman (Örn: `ping 192.168.1.50` dedin ve bilgisayarın bu IP'nin MAC adresini bilmiyor. ARP ve MAC tablolarında bu IP adresinin MAC adresi bulunmuyor).
* **Aynı Subnet Zorunluluğu:** ARP **sadece aynı subnet içindeki** cihazlar için atılır. Eğer gitmek istediğin IP seninle aynı subnet'te değilse, cihazın ARP'yi hedef IP için değil, kendi **Default Gateway**'i (yönlendiricisi) için atar.
* **Önbellek (Cache) Silindiğinde:** Bilgisayarlar öğrendikleri MAC adreslerini bir tabloda tutar (`arp -a` komutuyla görebilirsin). Bu kayıtlar genellikle birkaç dakika sonra eskir ve silinir. Silindiğinde tekrar ARP atılır.
* **Gratuitous ARP:** Bir cihaz ağa ilk bağlandığında, _"Bu IP bende, kimsede var mı?"_ demek için kimse sormadan ARP yayınlayabilir.

Bu süreçler genel de arkaplanda otomatize edilmiş şekilde tetiklenen mekanikler olduğundan bir ağ yöneticisi olarak örneğin bir **"Broadcast Storm"** (ağın aşırı trafikten kilitlenmesi) olduğunda bu mekanizmayı bilmek sorunu teşhis etmeni sağlar. Daha teknik ve detaylı bir ifadeyle; **ARP**, Layer 3 (Network - IP) ile Layer 2 (Data Link - MAC) arasındaki köprüdür. Cihaz elindeki IP bilgisini kullanarak "fiziksel adresi" bulmanı sağlar.

ARP süreci:
1.  **Sorgu (ARP Request)**: Senin bilgisayarın ağa bir paket bırakır. Bu paketin içindeki hedef MAC adresi `FF:FF:FF:FF:FF:FF` şeklindedir. Bu _"herkes okusun"_ demektir (**Broadcast**). Paketin içeriği şudur: _"IP adresi 192.168.1.20 olan arkadaş kimse, lütfen bana MAC adresini söylesin."_
2.  **Dinleme**: Ağdaki tüm cihazlar bu paketi alır ve açar. Ancak IP adresi kendisiyle eşleşmeyen herkes paketi çöpe atar.
3.  **Cevap (ARP Reply)**: Sadece o IP'ye sahip olan cihaz, _"O benim! MAC adresim de şudur: AA:BB:CC:11:22:33"_ der. Bu cevap doğrudan senin bilgisayarına gönderilir (**Unicast**).
4.  **Kayıt (ARP Cache)**: Bilgisayarın bu bilgiyi aldıktan sonra her seferinde ağda bağırmamak için bu bilgiyi ARP Tablosuna kaydeder.

Burada bilinmesi önem arz eden husus şudur ki; Broadcast mesajlar Router'ları (yönlendiricileri) geçemez;

* Eğer aradığın cihaz seninle aynı yerel ağda (Subnet) ise: ARP Broadcast ile ona ulaşabilirsin.
* Eğer aradığın cihaz başka bir ağda ise (Örneğin bir web sitesi): Bilgisayarın o IP için broadcast yapmaz. Onun yerine, paketleri dış dünyaya taşıyacak olan Default Gateway'in (Router'ın) MAC adresini sorar.

Özetle Mantık Şöyle İşler:
1.  **Kontrol:** Gitmek istediğim IP benimle aynı subnet'te mi?
2.  **Evet ise:** _"Bu IP'nin MAC adresi bende var mı?"_ (ARP Tablosuna bakılır).
3.  **Yok ise:** **Broadcast** yayın yap: _"192.168.1.50 kimse MAC adresini söylesin."_
4.  **Cevap:** Hedef cihaz kendi MAC adresini **Unicast** olarak sana döner.
5.  **Sonuç:** Veri transferi artık Unicast olarak devam eder.

Komut satırına (CMD) `arp -a` yazarsan, şu ana kadar bilgisayarının "bağırarak" öğrendiği ve hafızasına aldığı tüm IP-MAC eşleşmelerini görebilirsin.

### Unicast, Multicast, Broadcast vb. mekaniklerin pratik olarak denenebilirliği için uygun protokolü kullanan bir aracın gerekliliği üzerine

Unicast, Multicast gibi methotların nasıl çalıştıklarını anlamak için pratik olarak test yapılmak istenildiğinde bunlara uygun protokolü kullanan bir uygulama ve aracın kullanılması gereklidir. Örneğin şu soru doğal olarak sorulabilir; Multicast'i VXLAN, OSPF vb. dışında nasıl farklı biçimde test edebilirim? Multicast bir mekanik/davranıştır — asıl işi onu kullanan uygulama yapıyor. Direkt _"şu gruba katıl, birbirinizi bulun"_ diyemiyorsun bunu diyebilen bir uygulama, araya bir protokol girmesi lazım. VXLAN'da bu protokol VXLAN'ın kendisiydi. OSPF'te ki Hello paketleri için OSPF'ti. Multicast bir taşıma mekanizması, içini dolduran protokol asıl işi yapıyor. Örneğin unicast'i `ping` ile test edebiliriz çünkü ICMP protokolü taşıma mekanizması olarak arkaplan da unicast davranışı sergiliyor. Bu şekilde dolaylı olarak unicast davranışını da gözlemleyebiliriz. Ancak şu hataya düşülmemeli; örneğin Multicast davranışını test etmek için multicast için özel ayrılmış grup IP'lerini cihazların ağ arayüzlerine atayıp `ping` komutu ile bu grup IP'sini dinleyen her cihazın `ping` paketlerini alıp almadığına dair bir gözlem yapmaya kalkışmak hatalı olacaktır. Çünkü ilk olarak bir cihaza (örneğin bilgisayara) normal bir IP adresi (Unicast) verdiğin gibi bir Multicast IP'si (`224.0.0.0` - `239.255.255.255` arası) doğrudan "arayüz IP'si" olarak atanamaz. Cihazın yine kendi normal Unicast IP'si vardır (örn: `192.168.1.10`). Cihaz, **arka planda çalışan bir uygulama vasıtasıyla** switch/router'a der ki: _"Ben X.X.X.X multicast grubuna katılmak istiyorum, o gruba gelen trafikten bana da bir kopya gönder."_ Ancak bu şekilde Multicast davranışı gözlemlenebilir. 

```
Unicast  → ICMP (ping) ile test edebiliyorsun
Broadcast → ping 192.168.1.255 ile test edebiliyorsun
Multicast → ping ile test edemiyorsun çünkü
            multicast grubunu dinleyen bir uygulama/protokol gerekiyor
```

**Ping (ICMP) unicast protokolü** — tek hedefe gidiyor. Multicast adresine ping atsan bile karşı tarafın o grubu dinlemesi gerekiyor, aksi halde cevap vermez. Multicast'in çalışması için her iki tarafın da aynı grubu dinleyen bir uygulama çalıştırması şart.

VXLAN'da tam bunu yaptık:
- Her VTEP `239.1.1.1` grubunu dinledi
- Birbirleriyle VXLAN protokolü üzerinden konuştular
- Keşif gerçekleşti

Örneğin cihazlar `239.1.1.1` multicast grubuna üye oldu. Sen de üçüncü bir cihazdan (veya o iki cihazdan birinden) şu komutu yazdın `ping 239.1.1.1`. Arkada şu şekilde bir davranış oluşur;

- **Paketin Gönderilmesi (Multicast):** Ping (`ICMP Echo Request`) paketi yola çıkarken, hedef IP kısmına `239.1.1.1` yazılır. Yani paket **multicast olarak yola çıkar.** Switch, bu gruba üye olan o iki cihaza paketin birer kopyasını ulaştırır. Cihazlar paketi alır.
- **Cevabın Dönmesi (Unicast):** Paketi alan o iki cihaz, _"bana ping geldi, cevap vermeliyim"_ der. Cevap (`ICMP Echo Reply`) paketini hazırlarken, **kaynak olarak kendi gerçek (unicast) IP adreslerini**, hedef olarak da ping'i atan cihazın IP'sini yazarlar. Yani **cevaplar unicast olarak döner.**

Ardından teorik olarak ping attığında, o gruba üye olan cihazlardan ekrana tek tek cevap düşmesi gerekir. Ancak pratikte modern işletim sistemleri güvenlik ve ağ trafiğini koruma amacıyla buna farklı tepkiler verir:

- **Linux:** Multicast IP'sine ping attığında, o gruba üye olan tüm cihazlardan dönen cevapları ekranda alt alta görebilirsin. (Aynı anda birden fazla IP'den cevap geldiğini net bir şekilde izlersin).
- **Windows:** Windows varsayılan olarak **multicast ping isteklerine cevap vermez** (güvenlik duvarı/firewall engeline takılır). Ayrıca Windows'tan multicast ping atmaya çalıştığında genellikle ilk dönen cevabı gösterip diğerlerini göstermeyebilir.

**Broadcast**'i davranışını gözlemlemek için mevcut subnet'in broadcast adresine `ping` atılabilir. Böylece (bildiğimiz üzere broadcast tüm ağda ki cihazlara duyuru yapmak olduğundan) bu subnet'de ki her cihazdan `ping` cevabı alabiliriz. Ancak pratikte tam olarak öyle olmayabilir; Örneğin `192.168.1.255` broadcast adresine ping attığımızı varsayalım. Bu işlem tüm ağı etkileyebilecek bir durum olduğundan genel olarak ağda ki cihazlar geri cevap vermeyebilirler. Bunun sebebi eskiden bu yöntem hacker'lar tarafından bir saldırı olarak kullanılıyordu. Saldırgan, kaynak IP adresini kurbanın IP'siymiş gibi taklit edip (IP Spoofing), devasa bir ağın broadcast IP'sine ping atıyordu. Ağda ki binlerce cihaz aynı anda kurbana cevap gönderince, kurbanın bilgisayarı ve interneti kilitleniyordu. Buna **Smurf Attack** denir. Ancak artık Tıpkı multicast'te olduğu gibi, günümüzdeki birçok modern işletim sistemi (özellikle Windows ve güncel Linux dağıtımları) güvenlik duvarı (Firewall) kuralları gereği **broadcast üzerinden gelen ping isteklerine cevap vermez.** Dolayısıyla ping atsan bile, ağında 50 cihaz varsa sadece 3-5 tanesinden (güvenlik duvarı açık/esnek olanlardan) cevap alabilirsin. Diğerleri paketi alır ama çöpe atar.

### Multicast modu ile temel ve basit bir VXLAN topoloji örneği
Statik mod ile kurulan VXLAN topoloji örneğinden neredeyse hiçbir fark yok tek farklı kısım `vxlan10` ağ arayüzünde yapılan konfigürasyonel farklılık olacaktır. Statik modda `remote` ve `local` değerler manuel olarak veriliyordu. Ancak multicast modda tek bir grubun IP adresini her iki VTEP cihazında da belirterek birbirlerini buradan keşfedip etkileşim ve iletişim kurmaları sağlanacak. Bunun icin her iki cihazda da bu komut satırı uygulanmalıdır (hangi ethernet arayüz portuna bağlanılacağı topolojizinize göre değişkenlik gösterebilir burada her iki VTEP cihazı birbirlerine `eth1` üzerinden iletişime geçiyorlar);

Router-1 ve 2'de;
```
ip link add vxlan10 type vxlan id 10 group 239.1.1.1 dstport 4789 dev eth1
```

Statik modda `remote` ve `local` olarak her iki cihazda da komut satırında bunların Underlay IP değerlerini (`10.0.0.1, 10.0.0.2` gibi) belirtiyorduk. Ancak multicast'de tamamen bu ağ arayüzüne farklı bir grup IP'si atıyoruz. VXLAN Overlay olarak çalışıyorsa statik modda neden underlay IP değerlerini belirttik? Statik modda belirtilen bu Underlay IP'leri Overlay kısmının aslında hangi Underlay üzerinden çalışacağının belirtimidir. Her Overlay aslında bir Underlay üzerinde çalışır. VXLAN tüneli UDP üzerinden çalışıyor yani fiziksel ağ üzerinden gidiyor. Bu fiziksel ağda paket gönderebilmek için fiziksel hedef IP (Underlay) lazım. Başka türlü olması da zaten mümkün olamaz çünkü herşey fiziksel kablo aracılığıyla iletiliyor. Çözümlerimizi pahalılaştırmaktansa (özel donanım teçhizatları temini ve kurgusu) yazılımsal manipülasyonlarla (VLAN, VXLAN vb.) cihazın anlayış biçimini yönlendirip (Overlay gibi) istediğimiz sonucu daha ucuz ve kolay şekillerle alabiliriz. 
Statik modun Multicast moddan farkına gelirsek;

**Statik modda:**
`remote 10.0.0.2` diyorsun yani _"VXLAN paketlerini `10.0.0.2`'ye gönder."_ Tünel trafiği direkt o IP'ye unicast gidiyor. Ama sorun şu: 3. bir VTEP eklenirse ona da ayrıca `remote` tanımlamak gerekiyor (statik modun manuelliğinden kaynaklı dezavantajı).

**Multicast modda:**
`remote` yok onun yerine `group 239.1.1.1` var. VXLAN paketleri bu multicast grubuna gönderiliyor. Fiziksel ağdaki router multicast trafiğini gruba üye olan herkese dağıtıyor. Yani her iki modda da fiziksel ağ (underlay) kullanılıyor VXLAN paketi fiziksel olarak taşınmak zorunda. Fark şu:

```
Statik   → "şu spesifik IP'ye gönder" (unicast)
Multicast → "bu gruba gönder, kim dinliyorsa alsın" (multicast)
```

Underlay IP'leri her iki modda da kullanılıyor statik modda açıkça yazıyorsun, multicast modda ise fiziksel ağın multicast trafiği otomatik dağıtıyor. 
Bir multicast grubunda en fazla kaç host veya üye barındırılabiliyor? Yani bu multicast grup IP'sini dinleyen en fazla kaç cihaz olabilir? Bir limit var mı?  Teknik olarak bir multicast grubunda binlerce cihaz olabilir. Belirgin bir limit yok. Ama pratikte çok fazla VTEP aynı grupta olursa multicast trafiği artar ve ağ yükü artar. Nasıl buluşuyorlar?
VTEP `239.1.1.1` grubuna üye oluyor. Bir paket iletmek istediğinde bu gruba gönderiyor. Aynı grupta ki tüm VTEP'ler paketi alıyor ve _"bu benim için mi?"_ diye bakıyor. Bu sayede otomatik keşif ve iletim gerçekleşiyor. `vxlan10` sanal ağ arayüzü multicast mod ile ayarlandıktan sonra bridge ayari tıpkı statik mod örneğinde olduğu gibi yapılmalıdır. Tüm bu ayarların ardından host'lara aynı subnet'de olacak biçim de IP atamaları yapıldığı taktirde `ping` ile paketlerin iletimi test edilebilir.

### Bir ağ interface'inin detaylarını daha da fazla görme komutu

```
ip -d link show <interface>
```

`-d` (detail) flag'i ilgili arayüzün detaylarını gösteriyor. VXLAN arayüzünde çalıştırırsan VNI ID'si, grup IP'si, port numarası gibi tüm VXLAN yapılandırmasını görebilirsin.

örneğin;

```
ip -d link show vxlan10
```

komutu uygulandığında ağ arayüzünün hangi multicast grup IP'si kullanıldığı saptanabilir.

### Sanal ağ arayüzlerinin paket iletimi üzerine
Sanal ağ arayüzleri kendi başlarına farklı bir cihaza `ping` veya paket iletmek istediklerinde bunu doğal olarak kendi başlarına yapamazlar. Bu sanal ağ arayüzünü işlevsel/kullanılabilir hale getirebilmek için her zaman fiziksel bir IP/port/arayüz kullanması gereklidir (Her overlay'in aslında underlay gerekliliği). Bunun sebebi cihazlar birbirlerine kablo ile bağlı ve bunlar cihazin port'larına bağlı. Sanal ağ arayüzü, paketlerini fiziksel bir port üzerinden taşımalı ki diğer cihazlara erişebilsin. Bu yüzden OSPF, BGP veya VXLAN'da bu fiziksel IP/underlay kısmı kullanılıyor. Underlay ve overlay ayrımı da bu yüzden yapılıyor. Overlay kısmı underlay yapısını kullanan bir katman yalnızca. Eğer öyle ise neden tek bir katman kullanılmıyor? denilebilir. Bunun sebebi fiziksel yapı (underlay) değiştirildiğinde buna uygun ve manuel olarak yeniden cihazlarda konfigürasyon ayarı yapılması gereklidir. Bunun yerine bu yapı (underlay) değişse bile bu değişiklikten etkilenmeyecek sabit bir üst yapı veya bu değişikliği saptayabilecek sanal veya üst bir katman (overlay) olusturulup değişikliği hızlıca üst katmanda ki kurgulanmış sisteme adapte edecek şekilde tek bir konfigürasyon yapılması ve üstüne bunun otomatize hale getirilmesi aşırı basitlik ve kolaylık sağlar. İşte bu yüzden kendi kendini idare ve idame edebilen bir sisteme AS (autonomous system) özerk sistem deniliyor.

### Bir ağ arayüzüne (eth0, eth1 vb.) birden fazla IP adresi nasıl atanabiliyor? Ve durum böyle ise o halde bir cihazın birden fazla port'unun olmasının ne anlamı ve gereği var?
Bir ağ arayüzüne istediğin kadar IP adresi ekleyebilirsin. Bu, bu şekilde tasarlandığından ötürü böyle bir durumdur. Örneğin `eth0`'a hem `192.168.1.1/24` hem `10.0.0.1/30` atayabilirsin. Bu ikisi farklı subnet. Her biri kendine gelen trafiği karşılar. Part 2'de yaptığımız şey de buydu. `eth0`'a önce underlay IP'si atadık, sonra overlay için `30.1.1.1` atadık. Aynı fiziksel port, iki farklı IP. Birden fazla port'un gereği ise bazı şeylerin fiziksel ayrım gerektirmesinin gereğindendir:

**Farklı fiziksel ağlar**
- İki ayrı switch’e ya da iki farklı lokasyona bağlanmak için iki port gerekir.
- Tek port + çok IP bunu çözmez; çünkü kablo tektir.
**Performans (bant genişliği)**
- Tek portun kapasitesi sınırlıdır (örneğin 1 Gbps).
- İki port kullanırsan toplamda daha fazla throughput alabilirsin (link aggregation gibi).
**Yedeklilik (failover)**
- Bir port ya da kablo koparsa diğeri çalışmaya devam eder.
- Tek portta bu mümkün değil.
**Güvenlik / izolasyon**
- Örneğin: biri “internal network”, diğeri “DMZ”.
- Fiziksel ayrım bazen VLAN’dan bile daha güvenli kabul edilir.
**Farklı ağ teknolojileri**
- Biri Ethernet, diğeri fiber, diğeri management port olabilir.

Tek port'a atanan IP sayısı doğrudan hızı düşürmez. Darboğazı yaratan şey portun (arayüzün) fiziksel kapasitesi ve o porttan geçen toplam trafik miktarıdır. Tek bir arayüzün kapasitesi diyelim 1 Gbps. Bu arayüze ister 1 IP ver, ister 10 IP ver. Eğer toplam trafik 1 Gbps’yi aşmıyorsa sorun yok. Ama toplam trafik 1 Gbps’yi zorlamaya başlarsa, o zaman tıkanma olur. Tek portla hiç mi yapamayız? VLAN’lar ile tek portu bölüp farklı subnet’ler tanımlayabilirsin. Birden fazla IP atayabilirsin. Ama bu hâlâ; aynı fiziksel kabloya bağlıdır aynı bant genişliğini paylaşır aynı hata noktasına sahiptir. Özetle; birden fazla IP atayabilmek ile birden fazla port'a sahip olmak aslında farklı sorunları çözüyor. Tek bir porta birden fazla IP atayabilirsin ama o port hâlâ tek bir fiziksel bağlantı noktası. Şunu düşünürsek: Bir evin tek kapısı var ama o kapıya hem _"misafir girişi"_ hem _"kargo girişi"_ yazısı asarsan ne olur? Her şey yine o tek kapıdan geçmek zorunda. Bir sorun olursa her şey durur. Yani tek bir port'a birden fazla sorumluluk verilebilir ancak bir sorun oluşursa tüm işleyiş çöker. Birden fazla port'un asıl avantajları şunlar: Birincisi fiziksel izolasyon. Farklı portlar farklı fiziksel ağlara bağlanabilir. Bir port VTEP-2'ye giderken diğer port host'a gidebilir. İkincisi bant genişliği. Her port ayrı bir hat. Üçüncüsü yedeklilik bir port'da sorun oluşursa diğerleri çalışmaya devam ediyor. Birden fazla IP aynı porta atamak ise farklı bir amaç için kullanılıyor. Genellikle aynı fiziksel ağ üzerinde birden fazla rol üstlenmek için. Kısaca: Birden fazla port = farklı fiziksel bağlantılar. Birden fazla IP = aynı port üzerinde farklı roller.

### Bridge ağ arayüzüne bağlı port'ların incelenmesi
Bridge'in sanal bir switch olduğuna dair benzetme yapılmıştı. Aynı şekilde bu sanal switch'in port'lari `brctl showmacs <bridge_name>` şeklinde listelenip incelenebilir. Burada onemli bir kac noktalar mevcut;

İlki, uzun bir müddet paket iletimi (yani ping atılmazsa) cihazların MAC adresleri listede gözükmeyecektir. Çünkü bridge MAC adreslerini dinamik olarak öğreniyor. Tıpkı gerçek bir switch gibi. Bir cihaz paket gönderince bridge _"bu MAC adresi bu porttan geliyor"_ diye tabloya yazıyor. Paket gelmezse bilmiyor.

`is local?` kolonu;
Bu kolon bridge'e yerel olarak bağlı olan veya yerel olarak bağlı olmadan dolaylı şekilde öğrenilmiş cihazların, yerel olarak bağlandiysa `yes` dolaylı olarak elde edilmiş bir MAC adresi durumu varsa `no` ibarelerinin belirtildiği konumdur. Yani bridge hem yerel hem uzak cihazların MAC adreslerini biliyor. Sanki aynı switch'e bağlıymış gibi. Bu VXLAN'ın **Layer 2 uzatma** yaptığının kanıtıdır. Router-1'de Host-1 eth0'a bağlı. `eth0` bridge'e bağlı. Ama Host-1'in MAC adresi bridge tarafından `eth0` portundan öğrenildi — yani bridge için bu MAC adresi bir port üzerinden geldi, direkt bridge'in kendisine ait değil.

- `is local = yes` -> sadece bridge'in kendi MAC adresleri için geçerli — yani br0 arayüzünün kendisine ait MAC.
- `is local = no` -> ise bridge'in bir portundan öğrendiği MAC adresleri.

Yani hem Host-1 hem Host-2 bridge tarafından öğrenilmiş - biri `eth0`'dan, diğeri `vxlan10` tünelinden. İkisi de `no` çünkü ikisi de öğrenilmiş, bridge'in kendi MAC'i değil. Bilakis `yes` olanlara bakılacağı zaman Router-1 veya Router-2 cihazlarının `eth0` ve `vxlan10` olan arayüzlerinin MAC adresleri gözlemlenebilir. Bunlar bridge'in kendi portlarının MAC adresleri - bridge bunları zaten biliyor, öğrenmesi gerekmiyor. Bu yüzden paket iletimi zaman aşımı olsa dahi kaybolmuyorlar.

`ageing time` kolonu;
Kendisinden trafik alınmayan hostların MAC adreslerini tablodan otomatik olarak sileceğini (age-out edeceğini) söyler. MAC adresi tabloya yazıldıktan sonra belirli bir süre sonra siliniyor — çünkü o cihaz artık aktif olmayabilir. `ageing time` bu süreyi gösteriyor. Süre dolunca MAC tablodan siliniyor — bu yüzden ping atmayınca kayboluyor.

1. Hostun ping atmayı bırakıp pasif kaldığında 300 saniye sayacı başlar.
2. Süre dolunca VTEP üzerindeki Linux çekirdeği (Zebra vb. vasıtasıyla) bu MAC adresini lokal köprü (FDB) tablosundan siler.

Neden 300 Saniye? Ağ mühendisleri bu süreyi belirlerken iki büyük tehlike arasında bir denge kurmak zorundaydı:

- **Süreyi çok kısa yapsalardı (Örn: 10 saniye):** Cihazlar sürekli sessiz kalan hostların MAC adreslerini silecekti. Silinen bir MAC adresine paket göndermek istendiğinde, cihazlar (VTEP) hedefi bulabilmek için ağa sürekli **Flood** (MAC adresi için ARP) yapacaktı. Bu da ağda gereksiz bir trafik yükü (fırtına) yaratırdı.
- **Süreyi çok uzun yapsalardı (Örn: 2 saat veya 1 gün):** Ağda ki bir cihazın yer değiştirmesi durumunda (örneğin kablosunu söküp başka bir odaya/porta takması veya sanal makinenin başka bir sunucuya göç etmesi), eski yerdeki cihaz onun hala eski portta olduğunu zannedecekti. 2 saat boyunca o cihaza giden tüm paketler yanlış porta gönderilip kaybolacaktı (Blackhole). Ayrıca MAC tablosunun hafızası (CAM table) şişecekti.

İşte bu iki sorunun (Gereksiz Flood trafiği ve Blackhole) mükemmel kesişimi olarak ortalamasi, endüstri genelinde 300 saniye olarak kabul görmüştür.

### VXLAN'ın statik modda (unicast) veya dinamik multicast modda ayarlanması sonucunda bu modların farklari ve üstlendikleri roller
Bir uç cihaz (host) VXLAN ağı üzerinden bir paket gönderdiğinde ve paket VTEP cihazımıza geldiğinde gelen paketin hedef cihaza iletilebilmesi için bu hedef cihazin hangi VTEP cihazının arkasında olduğu bilinmesi gerekli. Yani VXLAN yapısında, bir uç cihaz (Host) ağa ilk kez paket gönderdiğinde, henüz hedef MAC adresinin hangi VTEP arkasında olduğu bilinmez. Bu duruma BUM (Broadcast, Unknown Unicast, Multicast) trafiği denir. Statik ve dinamik (multicast) modların bu süreçteki rolleri, bu **bilinmezliği** nasıl yönettikleriyle ilgilidir:

1. **Statik Mod (Static Ingress Replication)**
Statik modda, her VTEP cihazına diğer tüm uzak VTEP'lerin IP adresleri manuel olarak tanımlanır.
- **Paketin Yolculuğu:** Kaynak VTEP, gelen paketin hedefinin nerede olduğunu bilmediği için paketi kopyalar (replication).
- **Rolü:** Paketi, listesinde kayıtlı olan tüm uzak VTEP'lere tek tek (Unicast olarak) gönderir.
- **Dezavantajı:** Eğer ağda 50 tane VTEP varsa, kaynak VTEP aynı paketi 50 kez paketleyip göndermek zorundadır. Bu da bant genişliği ve CPU üzerinde ciddi yük oluşturur.

1. **Dinamik Multicast Modu**
Bu modda, VTEP'ler belirli bir VXLAN Segmenti (VNI) için ortak bir Multicast grubuna (örneğin: `239.1.1.1`) abone/üye olurlar.
- **Paketin Yolculuğu:** Kaynak VTEP, hedefi bilinmeyen paketi tek tek kopyalamak yerine, onu Multicast grubuna tek bir paket olarak gönderir. Tek bir paket olarak gönderilen paket her bir üye tarafından kendi taraflarında kopyalanır.
- **Rolü:** Ağdaki router'lar (Underlay ağ), bu paketi sadece o VNI ile ilgilenen ve o gruba üye olan VTEP'lere ulaştırır.
- **Öğrenme Süreci:** Paket hedefe ulaştığında, hedef VTEP cevap döner. Bu sırada kaynak VTEP, hedef MAC adresinin hangi IP'li VTEP'te olduğunu "öğrenir" ve bir sonraki iletişim artık Unicast olarak devam eder.

Her iki modun da buradaki temel rolü, ağın henüz bilmediği bir hedef için **sorup soruşturma (flooding)** işlemini yönetmektir. Statik mod bunu her kapıyı tek tek çalarak yaparken, Multicast modu bir hoparlörle tüm mahalleye seslenerek yapar. Veya statik modda bir bir haberi vermek icin tek tek herkesi rehberden telefonla aramak gerekir ama multicast ile bir konfreans görüşmesi veya grup araması ile herkesi tek bir ortamda toplayıp tek seferde haber verilir. Veya belirli bir radyo frekansı ayarlayıp bu radyo yayınına herkesle beraber katılmak gibi. Burada ki **ilk kez** ibaresi önemlidir çünkü amaç hedef cihazin MAC adresini belirli bir süreliğine (geçiçi olarak) mevcut cihazın (VTEP) ARP ve MAC tablolalarına kaydetmektir. Böylece bu ilk belirsizlik durumu belirli bir süreliğine aşıldıktan sonra Unicast iletişime dönülür çünkü artık hedef cihaza yeniden paket gelirse bunun icin yeniden statik mod veya dinamik mod kullanılmayacak bunun yerine ARP ve MAC tablolarında ki MAC adresi ve rota bilgisi kullanılacak (artık bilindiğinden) böylece uygun rota oluşturulacak. Bu yuzden bahsi geçen **belirsizlik** durumu için hangi methodun (statik (unicast), dinamik (multicast)) rolleneceğinin seçimi önem arz eder. Çünkü ARP ve MAC tabloları geçici olarak adres bilgilerini tuttuklarından yeniden hedef cihazin MAC adresini öğrenebilmek için ayarlanmış olan mod yöntemini kullanarak adresi elde edecek. Bu seçiminde performans bakımından ağı yormayacak biçimde seçilmesi önemlidir. Wireshark'da multicast grubu ile ilgili işlemleri görebilmek için GNS3'de ki VTEP cihazının MAC ve ARP tablolarının `flush` edilmesi gereklidir. Bundan sonra ARP atıldığı gözlemlenebilir. Linux'da ARP ve MAC tablolarını temizlemek için `flush` komutu kullanılabilir.

### Uç cihazdan gönderilen bir paketin VXLAN yapılı ağda ki yolculuğu
**Statik Mod (Head-end Replication)**
Cihaz A (VTEP 1 arkasında), Cihaz B’ye (VTEP 2 arkasında) paket göndermek istiyor ama henüz MAC adresini bilmiyor. Bu yüzden paket ilk kez gönderildiğinde;

1. **ARP Üretimi**: Cihaz A, hedef IP için bir ARP Request (Broadcast) paketi oluşturur ve VTEP 1'e gönderir.
2. **VTEP 1'in Karşılaması ve Öğrenmesi:** VTEP 1 paketi alır. Cihaz A'nın MAC adresini öğrenir. Kendi MAC Adres Tablosuna yazar.
3. **Replika Listesi Kontrolü:** VTEP 1, paketin bir **Broadcast** olduğunu anlar. Statik modda olduğu için konfigürasyonundaki kayitli kisma bakar. Burada VTEP 2 ve VTEP 3 gibi diğer uç noktaların IP adresleri manuel olarak kayıtlıdır.
4. **Head-end Replication (Kopyalama):** VTEP 1, gelen tek bir ARP paketini listedeki her bir uzak VTEP IP'si için tek tek kopyalar. Eğer listede 5 tane VTEP varsa, 5 ayrı paket oluşturur.
5. **VXLAN Kapsülleme (Encapsulation):** Her bir kopya için şu başlıkları ekler:
    -  _**VXLAN Header**_: VNI (Sanal Ağ Kimliği) eklenir.
    -  _**UDP Header:**_ Hedef port 4789 olarak belirlenir.
    -  _**Outer IP Header:**_ Kaynak IP: VTEP 1, Hedef IP: Listedeki ilgili uzak VTEP (Örn: VTEP 2).
6. **Underlay İletimi**: Bu paketler, fiziksel ağda (Spine/Core) normal birer Unicast IP paketi gibi yönlendirilir. Fiziksel ağ, içerisinde bir ARP paketi olduğunu bilmez.
7. **VTEP 2 (Hedef) Açma ve Öğrenme:** VTEP 2 paketi alır, dış IP başlığını soyar (Decapsulation). İçerideki orijinal ARP paketini görür. Bu esnada çok kritik bir şey yapar: _"Cihaz A'nın MAC adresi, VTEP 1 IP'sinin arkasındadır"_ bilgisini VXLAN tablosuna işler.
8. **Hedefe Teslim:** VTEP 2, orijinal ARP paketini Cihaz B'nin bulunduğu porta iletir.
9. **Geri Dönüş (Unicast):** Cihaz B, ARP Reply (Unicast) döner. VTEP 2 artık Cihaz A'nın ve VTEP 1'in nerede olduğunu bildiği için replikasyon yapmaz. Paketi doğrudan VTEP 1'e unicast olarak kapsülleyip gönderir.

**Multicast Modu (Flood and Learn)**
İlk kez paket gönderilecekse süreç şöyledir:
1. **Yerel Yakalama:** Cihaz A, bir ARP Request gönderir. Yerel VTEP (Leaf 1), bu broadcast paketini yakalar.
2. **VXLAN Kapsülleme (Encapsulation):** VTEP 1, bu orijinal paketi alır ve üzerine şunları ekler:
    -  _**VXLAN Header:**_ (VNI - Ağ kimliği)
    -  _**UDP Header:**_ (Port 4789)
    -  _**IP Header:**_ (Kaynak: VTEP 1 IP, Hedef: Multicast Grubu IP)
3. **Ağda Yayılma:** Paket, fiziksel iskelet (Underlay) üzerinden o multicast grubuna üye olan tüm VTEP'lere gider.
4. **Öğrenme ve Açma:** Diğer VTEP'ler (Leaf 2, 3 vb.) paketi açar (Decapsulation). VTEP 2 şunu öğrenir: _"Cihaz A'nın MAC adresi, VTEP 1'in IP'si arkasındadır."_ Bunu kendi tablosuna yazar.
5.  **Hedefe Teslim:** VTEP 2, paketi Cihaz B'ye iletir. Cihaz B, unicast bir ARP yanıtı döner. VTEP 2 artık VTEP 1'in yerini bildiği için bu sefer paketi doğrudan (Unicast) VTEP 1'e gönderir.

VXLAN'da **öğrenme** işlemi genellikle veri trafiği (data plane) üzerinden gerçekleşir. Yani bir VTEP, bir paketi decapsulate ettiği anda karşı tarafın hangi IP arkasında olduğunu öğrenmiş olur. Bu süreçte tabloların yönetimi, ağın stabilitesi için hayati önem taşır:

- **MAC Tablosu Girişleri:** VTEP'ler MAC adreslerini iki şekilde öğrenir:
  - Lokal: Kendi portuna takılı cihazdan gelen trafikle (Standart Switch gibi).
  - Uzak (Remote): Karşı VTEP'ten gelen VXLAN paketini açtığında (MAC + VTEP IP eşleşmesi).

- **Kayıtların Kaybolması (Aging):**
  - Cihazlar ve VTEP'ler, belirli bir süre (varsayılan genellikle 300 saniye / 5 dakika) trafik görmezse bu kayıtları siler.
  - Eğer Cihaz A ağdan çekilirse, VTEP 2'nin tablosundaki "A -> VTEP 1" kaydı 5 dakika sonra düşer. Bir sonraki istekte süreç baştan başlar.

Statik modun dezavantajı, **broadcast** trafiği her zaman tüm VTEP'lere gönderilir. Eğer 50 tane VTEP'iniz varsa, her bir ARP isteği için VTEP 1 tam 49 tane kopya paket üretmek zorunda kalır. Bu da CPU ve bant genişliği yükü demektir (Multicast modunun tercih edilme sebebi budur).

## Part 3

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

## Proje Teslimi ve Organizasyonu
PDF'in proje teslimi hakkında kastettiği şey şu; her cihazın yapılandırmasını ayrı bir dosyaya kaydetmeni istiyor. Her router ve host için elle yazılmış konfigürasyon dosyaları.
Dizin yapısına bakarsak — PDF'te şu dosyalar vardı:

```
P2/
├── P2.gns3project
├── _wil-1_g      ← router-1 config
├── _wil-1_host   ← host-1 config
├── _wil-1_s      ← switch config
├── _wil-2_g      ← router-2 config
└── ...
```

`_g` → router (gateway) config dosyası
`_host` → host config dosyası
`_s` → switch config dosyası

Bu dosyaların içine çalışan topolojinde ki cihazlara uyguladığın her ağ komutunu yazıyorsun — yorum satırlarıyla açıklayarak. Örneğin router-1 config dosyası:

```bash
# Router-1 VXLAN yapılandırması
# VTEP olarak çalışıyor

# VXLAN arayüzü oluştur
ip link add vxlan10 type vxlan id 10 group 239.1.1.1 dstport 4789 dev eth1

# Bridge oluştur
ip link add br0 type bridge
...
```
Bu sayede GNS3 projesi olmasa bile birisi bu dosyalara bakarak topolojiyi yeniden kurabilir.

 `.gns3project` ise topolojinin kendisi yani şemasi ancak içi doldurulmuş olarak değil. Bu GNS3'te `File -> Export Project` olarak `.gns3project` uzantısı şeklinde çıktısı alınabilir. PDF'te ki görsel de çıktı için hangi ayarların seçilmesi gerektiği belirtilmiş.

## Kaynaklar
- [GNS3 kurulumu ve sorunların çözümü](https://www.youtube.com/watch?v=SE--UqXLShg)
- [GNS3 kurulumu ve sorunların çözümü metinli](https://jono-moss.github.io/post/-gns3-install-debian-27-09-2024/)
