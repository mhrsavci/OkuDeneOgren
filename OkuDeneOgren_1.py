# Python p101



#### 1. Tanım ####

# Python bir yazılım-programlama dilidir.
# Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı tarafından 90' li yılların başında geliştirilmeye başlanmıştır.
# Python, C ve C++ gibi dillerin aksine derlenmeye gerek olmadan çalıştırılabilir.
# Python kolay öğrenilebilen, basit söz dizimine sahip bir dildir.
# Eger bir Python sürümü 2 sayısı ile baslıyorsa (mesela 2.7.11), o sürüm Python 2.x serisine
#   aittir. Yok eger bir Python sürümü 3 sayısı ile baslıyorsa (mesela 3.5.1), o sürüm Python 3.x
#   serisine aittir.

# Derleyici #
# Derleyici : Yüksek seviye bir programlama dilinde (high-level programming language) yazılmış bir kaynak kodun, başka bir hedef dile veya bilgisayarın/işlemcinin anlayabileceği makine diline tercümesini yapan bir programdır. Derleyiciler herhangi bir dil ile yazılmış olabilir. Her dil için bir veya daha fazla derleyici geliştirilebilir, bir dil için aynı zamanda hem derleyici hem yorumlayıcı yazılabilir.

# Yorumlayıcı #
# Yorumlayıcı : Yorumlayıcı, kaynak kodu komut komut okuyup üzerinde çalışılan makinenin komut setine çevirerek çalıştıran bir programdır. Yorumlanarak çalıştırılan yüksek seviyeli diller doğrudan yorumlanmazlar. Genellikle bir ara forma(Opcode,Bytecode vs.) derlenir ve bu kodlar yorumlanarak yerel makine diline çevrilir ve işletilir. Java, PHP, Python gibi yorumlanan diller aslında yorumlama aşamasına geçilmeden önce en az 1 kere derlenirler.

#### 2. Etkileşimli Kabuk ####

# Python kendine has komut sistemine benzer bir arayüze sahiptir. Bu arayüze Etkileşimli Kabuk (Interactive Shell) adı verilir.
# Python yazılım dilinde boşluk kullanımı çok önemlidir.
# Etkileşimli kabukta bulunan ‘>>>’ işaretinden sonra hiç boşluk bırakmadan komutlar yazılmalıdır. Aksi takdirde hata verecektir.
# Döngülerle birlikte birkaç yerde de boşluk kullanımına dikkat etmek gerekir. Çünkü bir döngü yazıldığında Python döngünün içerisinde olduğunu bir adet boşluk girintisinden anlar. Örneğin:

#    while(True):
#      True şartı sağlandığında gerçekleştirilecek ifadeler bu kısımda yazılır.


#### 3. Karakter Dizileri ####

# Tüm yazılım dillerinde olduğu gibi Python dilinde de verinin hangi tipte olduğu önemlidir. Üzerinde çalışılan verinin hangi tipte olduğunun bilinmemesi yapılacak olan işlemlerin de bilinmemesi demektir.
# Python’ da her veri tipinin belli başlı özellikleri vardır.
# Python’ da tırnak içinde gösterilen her şey bir Karakter Dizisi’ dir.
# Python’ da boş karakter dizisi ile bir adet boşluktan oluşan karakter dizisi birbirlerinden farklı kavramlardır.
# Boş karakter dizisinin içerisinde hiçbir öğe barındırmaz ve bu nedenle indeks yapısı da yoktur.Yani boş karakter dizisinin ilk indeksindeki eleman çağırılırsa hata ile karşılaşılır. 
# Bir adet boşluktan oluşan karakter dizisinin adından da anlaşılacağı gibi bir adet elemanı bulunur.

# Eğer herhangi bir verinin tipi kontrol edilmek isteniyorsa  type() adlı bir fonksiyon kullanılabilir.

veriTipi=type("Python bir programlama dilidir.") # type fonksiyonu içerisine yazılan ifadenin hangi veri tipinde olduğunu döndürür. Döndürülen değer veriTipi adlı değişkene atandı.
print(veriTipi) # veriTipi adlı değişken ekrana yazdırıldı.

# Python’ da tanımlanan herhangi bir karakter aynı zamanda bir karakter dizisidir.

# Herhangi bir karakterin uzunluğu len() fonksiyonu ile kolayca öğrenilebilir.

karakterSayisi = len("Python bir programlama dilidir.") # len fonksiyonu içerisine yazılan karakter dizisinin karakter uzunluğunu döndürür. Döndürülen değer karakterSayisi adlı değişkene atandı.
print(karakterSayisi) # karakterSayisi adlı değişken ekrana yazdırıldı.


# Python’ da bazı değerler sonradan da kullanılmak istenilebilir bu nedenle değişkenler tanımlanır. Değişkenler değerlere atanmış adlar olarak tanımlanabilir.  Değişken adı tanımlanırken uyulması gereken kurallar mevcuttur:

## 1. Değişken adları bir sayı ile başlamaz. (Yanlış Kullanım: 1_kilo_seker)
## 2. Değişken adları aritmetik işleçlerle başlayamaz (Yanlış Kullanım: +deger)
## 3. Değişken adları ya bir alfabe harfiyle ya da _ işaretiyle başlamalıdır.
## 4. Değişken adlarında Türkçe karakterler kullanılmamalıdır. (Yanlış Kullanım: değişken)
## 5. Python içerisinde kullanılan anahtar kelimeler değişken adı olarak kullanılamaz. (Örneğin: False, None, True, and, as, finally …vs)

# Python içerisinde kullanılan anahtar kelimelere erişmek için:

import keyword # import ile keyword kütüphanesi projeye dahil edildi.
anahtarKelimeler=keyword.kwlist # keyword kütüphanesinin kwlist özelliği kullanılarak python da belirli anahtar kelimeler anahtarKelimeler değişkenine atandı.
print(anahtarKelimeler)

## 6. Python dilinde kullanılan fonksiyonların isimleri eğer bir değişken ismi olarak tanımlanırsa fonksiyon kullanılırken TypeError adlı hata alınır. Böyle hatalarda del öneki kullanılarak tanımlanan değişken silinebilir.
type=23 # Yanlış kullanım.
del type # type adıyla tanımlanan değişken silindi.

## 7. Değişken adları belirlenirken boşluk karakteri kullanılamaz. (Yanlış kullanım: kullanıcı adı= "python")

# Tanımlanmış olan iki farklı değişkenin değerlerini birbirleri ile değiştirmek için:

sayi1 = 35
sayi2 = 77

sayi1, sayi2 = sayi2, sayi1 # sayi1 değişkeninin değeri ile sayi2 değişkeninin değeri birbirleriyle değiştirildi.

print("sayi1: {0}, sayi2: {1} ".format(sayi1,sayi2)) # Tırnak içerisine yazılan ifade içerisinde {0} ve {1} göstergeleri yerine yazılacak değerler sonradan format fonksiyonu ile sırasıyla belirlenir.


# Etkileşimli kabukta çalışırken yapılan son işlemin çıktısı "_ " (alt tire) ile   hafızadan çağırılabilir. Burası etkileşimli kabuk değildir. Burası python projesinin sayfasıdır ve çalıştırıldığında sonuçları etkileşimli kabukta gösterilir.

# Python ile kod yazmak için Microsoft Word veya OpenOWce.Org OOWriter gibi, belgeleri ikili (binary) düzende kaydeden programlar uygun degildir. Kullanılacak metin düzenleyici, belgeleri düz metin (plain text ) biçiminde kaydedebilmeli. 






