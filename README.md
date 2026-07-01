# BADASS

<img src="Images/spiderweb.gif" align="right" height="500">

Bu proje de bir veri merkezi ağ altyapısının nasıl tasarlanması gerektiğinin temel pratik uygulamaları GNS3 programı ile simüle edilerek kurgu edilmesi istenmektedir. Aslında daha çok emüle etmek denilebilir. Bu sayede ağ yöneticiliği dünyası hakkında teorik olarak pek çok kavram ve yenilik edinilmiş olacak ve ayrıca pratik olarak da pek çok teknik ve çözümsel yaklaşımlar ile yeni perspektifler edinilmiş olacaktır. Teorik olarak internetin nasıl çalıştığı, özerk sistemlerin (AS) ne olduğu, ağ cihazlarının ne olduğu ve birbirleri ile olan etkileşimleri vb. örnekler verilebilir. Aynı şekilde az önce sıralanan edinimlerin pratik açıdan teknik anlam da arkaplan da nasıl çalıştığı ve nasıl dizayn edilmesi gerektiğinin öğrenilmesi hedeflenmektedir. Ancak ne olursa olsun teknik anlamda veri merkezlerinde oluşan sorunlar bizzat ve doğrudan yaşanılmadıkça bu sorunlar üzerine geliştirilen BGP EVPN, VLAN, VXLAN, VPLS, MPLS vb. teknik yaklaşımlarının tam anlamıyla anlaşılmasının zor olduğu kanaatindeyim. Bu yaklaşımlar ağ mühendisleri tarafından belirli sorunların üstesinden gelinmek amacıyla düşünülmüş ve geliştirilmiş tekniklerdir. Bu yüzden bu projenin bu tekniklerin nasıl kullanılması gerektiğini değil belirli sorunlar yaşanıldığında bu sorunların nasıl üstesinden gelinmesi gerektiğinin edinimini öğretmeyi hedeflemesi gerektiği kanaatindeyim. Bu model daha mühendissel/tekniker bir bakış açısı edinimi sağlayabilirdi. Tabii bunun için bizzat saha da olmak gerekli ve bu mümkün olamadığından belki de bu proje bu kadarını bizlere sunmuştur. Bunların yanı sıra ağ kavramları çok soyut kavramlar olduğundan öğrenildiği düşünülen şey farklı bir bağlamda çok farklı biçim de ele alınabilir. Bu da öğrenildiği düşünülen şey hakkında gerçekten öğrenilip öğrenilmediğine dair şüpheler oluşturabilir. Bunu izah etmek gerekirse; Multicast'i üçgen olarak öğrendiğinizi varsayın (Multicast = üçgen). Ancak Multicast'i farklı bir bağlam da ele aldığınız da aslında Multicast'in kare olduğunu öğreniyorsunuz. Daha sonra yine farklı bir bağlam da ele aldığınızda aslında Multicast yıldızmış. Tüm bunlar fark edildiğinde Multicast'in bağlamsal duruma göre hem teknik hem de ifadesel olarak esnek bir kavram olduğu sonucuna varabilirsiniz. Bu C'de pointer öğrendiğinizi zannetmenize örnek verilebilir :d. Farklı bir kimseden pointer konusunu dinlediğinizde zihninizde ki kavramla örtüşmediğini ancak pointer'ı anlatan kimsenin de çok tutarlı bir şekilde izahat de bulunduğunu fark edip hangisinin doğru olduğunun sorgulamasına düşebilirsiniz. Bu hem siz hem de diğer kimsenin pointer'ı kavramını zihin de nasıl ilişkilendiriğine bağlı bir durumdur. Her iki kişi de zihnin de pointer kavramını tutarlı bir biçim de ilişkilendirmiş ama bunu birbirlerine anlatmaya çalıştıklarında örtüşmediğini fark ederler. Ama günün sonunda aslında aynı şeyden bahsediyorlardır. Özetle belki de tüm bunların sebebi ağ kavramlarının bağlamsal ve anlamsal olarak iç içe geçmesi ve tam anlamıyla bir literatür standardı oluşturulamaması durumu yüzünden her üretici (Cisco, Juniper, FRR vb.) kendi terminolojisini ve isimlendirmesini kullanıyor bu da karmaşıklığın artmasına sebep oluyordur.

Yazımız da tıpkı proje dokümanında olduğu gibi bölüm bölüm ve her bölüm bir öncekinin devamı niteliğinde bir ilerleme yapılacaktır. Her bölüm de karşılaşılan sorunlar dile getirilecek ve bunlara yönelik ne gibi çözümler uygulanabileceği açıklanacaktır. Ayrıca sadece sorun ve çözümler verilmeyecek proje dokümanın belirttiği kavramlara değinilecek ve öğrendiğimiz yeni bilgiler ışığında internet üzerinden bizlerin nasıl bir e-ticaret sitesine ulaştığına dair örnek bir diyagrama yer verilecektir. 

## İçindekiler

  - ### [Part 1: Docker ile GNS3 konfigrasyonu](P1/README.md)
    
    <img src="Images/part1.png" style="width: 45%; height: auto;">
    
    Bu bölüm de mevcut sistemimize GNS3'ün nasıl kurulacağını ve Docker entegrasyonunu nasıl gerçekleşemesi gerektiği açıklanacaktır. Ayrıca GNS3'ün nasıl kullanılması gerektiği ve programda ki terminolojilerin ne anlama geldiği tarzında açıklamalar yapılacaktır.

  - ### [Part 2: VXLAN'ı keşfetmek](P2/README.md)
    
    <img src="Images/part2.png" style="width: 45%; height: auto;">
    
    Bu bölüm aynı ağda ki cihazların birbirlerinden nasıl izole edilebilceğini açıklanmakta ve farklı subnet'lerde (uzak ve farklı lokasyonlarda) bulunan cihazların sanal bir ağ katmanı aracılığıyla nasıl sanki aynı subnetteymiş gibi davrandıkları açıklanacaktır.

  - ### [Part 3: EVPN ile BGP'yi keşfetmek](P3/README.md)
    
    <img src="Images/part3.png" style="width: 45%; height: auto;"> 

  - ### [E-ticaret sitesine yolculuk](#proje-teslimi-ve-organizasyonu)

  - ### [Proje Teslimi ve Organizasyonu](#proje-teslimi-ve-organizasyonu)

  - ### [Kaynaklar](#kaynaklar)



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
- [Taylan Bildik Temel Ağ Eğitimine Giriş video serisi](https://youtu.be/d30mdlHGvdg?si=KpXxcb6bgNdGbabk)
- [IT MasterMind "Autonomous System (AS) Kavramı" video'su](https://youtu.be/xgQT84IxhIw?si=SKGgv-PtVBFxvZLZ)
- [TheBitsShow "Telnet and SSH - Animated" video'su](https://youtu.be/y-6KjigFNOM?si=blV5fPf49sQb1SGe)
- [Mehmet Ceyhan YAĞLI "CCNP RS -  Route  -  3.55 -  OSPF" serisinin bir kaç videosu](https://youtu.be/fpJLtmUGheM?si=sbUcURk8WG6aS1GJ)
- [Ömer Bektaş "İnternet nasıl çalışıyor bölüm 1" video'su 🌍
](https://youtu.be/_RmdrJNNHF0?si=Unki8EJocAxDoOJd)
- [Ömer Bektaş OSI video'su](https://youtu.be/LKUNExyhPyo?si=-2NBiZCat_MUOKfy)
- [MDUZGUNN "40-) BGP Dinamik Routing Protokolü" video'su](https://youtu.be/N9agdL72RaE?si=YKu1Lew_-Bir9i9d)
- [IT MasterMind "VLAN Nedir ve Neden Kullanılır" video'su](https://youtu.be/yC5BMBDeQWw?si=8NjPJWZwtjIHlyuJ)
