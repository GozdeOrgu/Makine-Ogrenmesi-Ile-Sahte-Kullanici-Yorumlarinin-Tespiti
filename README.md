# Makine Öğrenme Yöntemleriyle Sahte Kullanıcı Yorumlarının Tespiti

<img src="https://i.hizliresim.com/b7h62o.jpg">

<h3>Proje İçeriği</h3>

<ul>

<li>1- Giriş</li>
<li>2- Data Setinin Oluşturulması</li>
<li>3- Proje İçin Kullanılan Yöntemler</li>
<li>3.1- LSTM</li>
<li>3.2- Lojistik Regrasyon</li>
<li>4- Kullanılan Algoritmaların Karşılaştırılması (Sonuç)</li>

</ul>

<h2>1- Giriş</h2>

E-ticaret sistemi çok geliştiği için ürünler hakkında birçok yorum yapılmaktadır. Yapay zekanın gelişmesiyle birlikte verilerin gerçekliği hakkında şüpheler başlamıştır. Bu projede bu soruna çözüm aranmaktadır. Geliştirilen sistem şu şekilde çalışmaktadır. Öncelikle klavyeden bir giriş alınır. Daha sonra eğitilmiş modelimiz bunun makine yorumu mu (sahte yorum) yoksa insan yorumu mu olduğunu tespit etmektedir.


<h2>2- Veri Setinin Oluşturulması</h2>
Data setinin Türkçe olması için datasetini kendimiz oluşturduk. Datasetinde toplamda 2549 adet yorum bulunmaktadır. Bu verilerin <b>1200</b> tanesi gerçek kullanıcı yorumudur. Geriye kalan veriler fake olarak üretilmiştir. Fake yorumlar ise GRU (Lstm nöron çeşiti) ile geliştirilmiştir. https://github.com/Aksoylu/Eye-Blink-Detector-Deep-Learning adresindeki bir proje kaynak alınarak 1349 adet fake veri üretilmiştir.

Doğal yorumlar hepsiburada'da yer alan ürün yorumlarından toplanmıştır. Genellikle maskara, ayakkabı, çanta, telefon, kulaklık gibi ürünlerin yorumlarından oluşmuştur. Datasetimizi oluştururken <b>Kullanıcı yorumları 1</b> ile ifade edilirken <b>fake yorumlar 0</b> ile gösterilmiştir. Bunun için oluşturulan datasetinde <b>yorum</b> ve <b>etiket</b> sütunları bulunmaktadır.

<h2>3- Proje İçin Kullanılan Algoritmalar</h2>

Bu projede iki adet algoritma kullanılmıştır. Bunlardan bir tanesi <b>LSTM</b> diğeri ise <b>Lojistik Regrasyondur</b>. İki adet algoritma kullanılma sebebi ise hangi algoritmanın daha iyi sonuç vereceğini tespit etmektir.

Bu algoritmaların karşılaştırılması ve sonuçları ilgili kısımlarda anlatılacaktır.
LSTM yapısı itibariyle bir model eğitilirken zaman almaktadır. Bu algoritmayı tercih etmemizin sebebi ise daha iyi öğrenme gerçekleşeceğini ilgili makaleleri incelememizdir. Biz de denemek için öncelikle sistemimizi bu şekilde geliştirdik.
<h3>3.1- LSTM (Long-Short Term Memory) Algoritması</h3>
    
Öncelikle bilindiği üzere LSTM derin öğrenme algoritmalarından en popüleri olan RNN(Recurrent Neural Network)'nin uzun süreli bağımlılıkları öğrenebildiği özel bir türüdür. Ayrıca uzun kısa süreli bellek derin öğrenme alanında kullanılan yapay bir tekrarlayan sinir ağı mimarisidir. Standart ileri beslemeli sinir ağlarının aksine, LSTM'nin geri bildirim bağlantıları vardır. Yalnızca tek veri noktalarını değil, aynı zamanda tüm veri dizilerini işleyebilir. 
LSTM lerin tasarlanma amacı uzun vadeli bağımlılık sorununu önlemektir. Varsayımsal olarak bilgiyi uzun süreler boyunca hatırlarlar.

Tüm tekrarlayan sinir ağları, sinir ağının tekrar eden modüllerinin bir zinciridir. 

Standart bir RNN’deki tekrarlayan modül tek bir katman içerir. LSTM’ler de bu zincir benzeri yapıya sahiptir, ancak tek bir nöral ağ katmanı yerine 4 tanesine sahiptir.

<b>Ayrıca LSTM'in bir katında 128 adet bellek hücresi bulunur.</b>

<h2>3.2- Lojistik Regresyon Algoritması</h2>
<b>Lojistik regresyon,</b> bir sonucu belirleyen bir veya daha fazla bağımsız değişken bulunan bir veri kümesini analiz etmek için kullanılan istatistiksel bir yöntemdir. 

<b>Sonuç, ikili bir değişkenle ölçülür (yalnızca iki olası sonuç vardır). Yani 1 (Doğru, başarı), ya da 0 (Yanlış, hata) olarak kodlanmış verileri içerir.</b>

Amacı, iki yönlü karakteristiği (bağımlı değişken = yanıt veya sonuç değişkeni) ile ilgili bir dizi bağımsız (öngörücü veya açıklayıcı) değişken arasındaki ilişkiyi tanımlamak için en uygun (henüz biyolojik olarak makul) modeli bulmaktır. 

Lojistik regresyon, ilgi karakteristiklerinin varlığının olasılığını logit dönüşümünü tahmin etmek için bir formülün katsayılarını (ve standart hatalarını ve önem seviyelerini) üretir.

* Projemizde iki adet parametre olduğu için yani ya sahte yorum ya da makine yorumu diye karar verileceği için bu algoritmanın kullanılmasının uygun olacağına karar verdik

<h2>4- Algoritmaların Karşılaştırılması (Sonuç)</h2>

<blockquote cite="https://www.huxley.net/bnw/four.html">Lojistik Regresyon algoritması için geliştirilen sistemin doğruluk oranı daha yüksektir. Lstm kullanarak sistemi eğitirken yaklaşık 15 dakikada model geliştirilmiştir. Lojistik regresyon daha basit yapıda olduğu için 5 saniyede model oluşturulmuştur. Böyle bir proje gerçekleştirilirken maliyet açısından değerlendirilecek olursa <b>Lojistik regresyonu</b> tercih edilmelidir. Ayrıca bu proje 0 ya da 1 gibi değerlere yakın olduğu için Lojistik Regrasyon daha uygun bir algoritmadır.</blockquote>
