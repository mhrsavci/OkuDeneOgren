# Python p108


##### 8. KARAKTER DiZiLERiNİN METOTLARI #####


karakter= "Python'da Karakter Dizileri"

print(karakter.lower()) # -> karakter değişkeni içerisindeki string değerinin tüm harflerini küçültür.

print(karakter.upper()) # -> karakter değişkeni içerisindeki string değerin tüm harflerini büyütür.

# isupper() -> Harflerin büyük olup olmadığını sorgular.

print(karakter.isupper())


# islower() -> Harflerin küçük olup olmadığını sorgular.

print(karakter.islower())


# endswith() -> Bir karakter dizisinin hangi karakter ile bittiğini sorgular.

# startswith() -> Bir karakter dizisinin hangi karakter ile başladığını sorgular.

# capitalize() -> Bir karakterin sadece ilk harfini büyük yapar.

# title() -> Bir karakter içerisinde yer alan tüm kelimeleri büyük harfle başlatır.

print(karakter.capitalize())

print(karakter.title())



# swapcase() -> Bir karakter içerisinde büyük yazılan harfleri küçük, küçük yazılan harfleri büyük yapar.

print(karakter.swapcase())

######################  TABLO 1 ###########################
###########################################################
## ‘ ‘	boşluk karakteri                           
## \t	sekme (TAB) oluşturan kaçış dizisi   
## \n	satır başına geçiren kaçış dizisi    
## \r	imleci aynı satırın başına döndüren kaçış dizisi 
## \v	düşey sekme oluşturan kaçış dizisi   
## \f	yeni bir sayfaya geçiren kaçış dizisi   
###########################################################

# strip() -> Eğer özel bir karakter belirtilmezse bir karakterin başında ve sonunda bulunan Tablo 1 de geçen ifadeleri temizler.

print(karakter.strip())

# lstrip() -> Eğer özel bir karakter belirtilmezse bir karakterin sol tarafında bulunan Tablo 1 de geçen ifadeleri temizler.
# rstrip() -> Eğer özel bir karakter belirtilmezse bir karakterin sağ tarafında bulunan Tablo 1 de geçen ifadeleri temizler.


# join() -> Karakterleri birleştirmek için kullanılır:

ifade= ["Python","Makine","Öğrenmesi"] # Karakter dizisi oluşturuldu.

aralikDegeri=" " # Dizi elemanlarını birleştirirken araya gelecek karakter.

ifadeTop=aralikDegeri.join(ifade) # aralikDegeri karakteri aralara gelecek şekilde ifade karakter dizisinin elemanlarını join() metodu birleştirdi.

print(ifadeTop)


# count() -> Bir karakter içerisinde belirtilen karakterin sayısını döndürür.

aramaMetni="""Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli
yüksek seviyeli bir programlama dilidir. Girintilere dayalı basit sözdizimi,
dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.
Bu da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama
yapılmaya başlanabilen bir dil olma özelliği kazandırır."""

iSayisi=aramaMetni.count("i") # aramaMetni içerisinde bulunan "i" harfinin sayısını "iSayisi" adlı değişkene atar.

print(iSayisi)


# index() -> Bir karakter dizisi içinde belirtilen karakterin ilk konumunı döndürür.

print(aramaMetni.index("m")) # aramaMetni içerisinde bulunan ilk "m" harfinin indeks numarasını döndürür. Saymaya sıfırdan başlar.

# Eğer index metodu aradığı karakteri ilgili karakter dizisinde bulamazsa ValueError hatası verir.

# print(aramaMetni.index('"'))

# find() -> Bir karakter dizisi içinde kendisine belirtilen karakteri arar. index() metodu ile arasındaki tek fark eğer karakter dizisi içinde aradığı karakteri bulamaz ise find() metodu -1 döndürür.

# rjust() & ljust() -> Bir karakter metnini sağa ve sola yaslamak için kullanılır.


# print(aramaMetni.rjust(len(aramaMetni),".")) # rjust() fonksiyonu kendisine verilen karakter sayısı kadar bir yer oluşturur geriye kalan kısımları(eğer kalırsa) da kendisi "." işaretiyle tamamlar.

# print(aramaMetni.rjust(20,".")) # Eğer rjust() veya ljust() fonksiyonuna hizalanan metinin uzunluğuna eşit veya daha az karakter sayısı verilirse karakter dizisi üzerinde bir değişiklik yapılmaz.

# print(aramaMetni.rjust(500,".")) # aramaMetni karakter dizisinin uzunluğunu 500 değerinden çıkarır ve geri kalanı "." işaretiyle tamamlar.
 
# print(aramaMetni.ljust(500,"."))

# encode() # Bu metot yardımıyla karakter dizileri istenilen kodlama sistemine göre kodlanabilir. Python 3.x’te varsayılan karakter kodlaması utf-8‘dir.

print("Normal Hal : {0}\nKodlanmış Hal : {1}".format(karakter,karakter.encode("cp1254")))
