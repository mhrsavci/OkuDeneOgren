# Python p124

#### 23. GÖMÜLÜ FONKSİYONLAR - 2 #####

## İfade ve Deyim 

# İfade : İngilizcede expression denen ‘ifadeler’, bir değer üretmek için kullanılan kod parçalarıdır. Karakter dizileri, sayılar, isleçler, diğer veri tipleri, liste üreteçleri, sözlük üreteçleri, küme üreteçleri, fonksiyonlar hep birer ifadedir.

# Deyim : İngilizcede statement olarak adlandırılan ‘deyimler’ ise ifadeleri de kapsayan daha genis bir kavramdır. Buna göre bütün ifadeler aynı zamanda birer deyimdir. Daha doğrusu, ifadelerin bir araya gelmesi ile deyimler oluşturulabilir.

# Örneğin sadece tek başına >> 5 << sayısı int tipinde bir ifadedir. Fakat >> a = 5 << ifadelerden oluşan bir deyimdir ve bu deyim a' yi bir değişken olarak tanımlamış yani bir değer üretmiştir.

## eval()

# Python'da "deyim" ve "ifade" kavramlarını kolay ayırt etmenin bir diğer yolu da eval() fonksiyonudur. Bir şey eval() fonksiyonuna parametre olarak verilir de hata alınmaz ise o parametre bir ifadedir.


eval("a=5")  # -> deyim # hata verir.

eval("5+45") # -> ifade # hata vermez. 50 değerini döner.


## exec() 

# exec() fonksiyonu deyimleri parametre olarak alabilir.

exec("a=5") # -> ifade # hata vermez a değeri sorgulandığında 5 olduğu görülür. 

exec("4+5") # -> deyim # hata vermez sonuç da vermez.


## globals() ve locals()

# Python programlama dilinde isim alanları sözlük tipinde bir veridir. Örnegin global isim alanı basit bir sözlükten ibarettir.Global isim alanları da globals() fonksiyonu ile çağırılır. Bu fonksiyon sözlük tipinde veri döner.

globals() # -> global isim alanlarını döner.

locals() # -> local isim alanlarını döner.

# Belirli bir ortama değişken oluşturma: 

ortam={}
exec("x=2")
exec("x=12",ortam) # ortam isimli ayrı bir yerde x değeri oluşturuldu. global kısımdaki x değeri 2 ortam kısmındaki x değeri de 12 olarak atandı.


# license() -> Python lisansına ilişkin detaylı bilgileri döndürür.

# dir() -> Parametresiz olarak kullanıldığında mevcut isim alanındaki ögeleri döndürür. globals() ve locals() fonksiyonlarına benzer. globals() ve locals() fonksiyonları birer sözlük döndürürken dir() fonskiyonu liste döndürür.

# dir() # Fonksiyona parametre olarak verilen ögenin yeteneklerini döndürür. Öge hangi fonksiyonları, metotları kullanabilir vs.

# divmod(17,3) # Output:(5,2) : 17 sayısının 3 sayısına bölümünden bölüm 5 kalan 2 olarak döner.

# enumerate() -> Nesneleri numaralandırmak için kullanılır.

enumerate("karakter dizisi") # Bu şekilde iterable bir nesne döner. Bir döngü yardımıyla veya list() fonksiyonu ile elemanlarına ulaşılabilir hale getirilir.

list(enumerate("karakter dizisi")) # Output : [(0, 'k'), (1, 'a'), (2, 'r'), (3, 'a'), (4, 'k'), (5, 't'), (6, 'e'), (7, 'r'), (8, ' '), (9, 'd'), (10, 'i'), (11, 'z'), (12, 'i'), (13, 's'), (14, 'i')]

# exit() -> O anda çalışan programdan çıkmayı sağlar.

# help() -> Herhangi bir nesnenin dokümante edilmiş nesnenin nasıl çalıştığına dair bilgilerini döndürür.

# id() -> Herhangi bir nesnenin kimliğini döndürür. Python' da her nesnenin bir kimlik bilgisi vardır.


   
   





