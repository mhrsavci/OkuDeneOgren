# Python p126

#### 23. GÖMÜLÜ FONKSİYONLAR - 4 #####

# pow(2,3) #-> 2^3 sonucunu döndürür.
# pow(2,3,2) # -> 2^3 sonucunu 2 modülüne göre hesaplar döndürür.

# print(deg1,deg2,...degx,sep="",end="",file="",flush="") Fonksiyonu : 

# degx : Çıktı verilecek degerlerin ne oldugunu belirtir. Buraya 256 adete kadar değer yazılabilir.
# sep :  Çıktı verilirken degerlerin arasına hangi karakterin yerleştirileceğini belirtir. Bu deger öntanımlı olarak bosluk karakteridir.
# end : Çıktı verilecek son degerin ardından hangi karakterin ilistirilecegini belirtir. Bu deger öntanımlı olarak satır bası (\n) karakteridir.
# file : Çıktıların hangi dosyaya yazılacagını belirtir. Öntanımlı olarak bu parametrenin degeri sys.stdout'tur. Yani print() fonksiyonu çıktılarını öntanımlı olarak standart çıktı konumuna gönderir.

# flush : Bildiginiz gibi, herhangi bir dosyaya yazma islemi sırasında dosyaya yazılacak degerler öncelikle tampona alınır. İslem tamamlandıktan sonra tampondaki bu degerler topluca dosyaya aktarılır.İste bu parametre, degerleri tampona almadan dogrudan dosyaya gönderebilmemizi saglar. Bu parametrenin öntanımlı degeri False'tur.Yani degerler dosyaya yazılmadan önce öntanımlı olarak öncelikle tampona gider. Ama eger biz bu parametrenin degerini True olarak degistirirsek, değerler dogrudan dosyaya yazılır.

# quit() # -> Programdan çıkmak için kullanılır.

# range() # -> Belirli bir aralıktaki sayıları listelemek için kullanılır.

# range(başlangıç, bitiş, artım) # "başlangıç" değerinden "bitiş" değerine kadar "artım" değeri kadar sayılrı getirir. range() fonksiyonunun ön tanımlı başlangıç değeri 0'dır. Ön tanımlı artım değeri de 1'dir

# sorted() # -> Bir dizi içerisindeki elemanları belirli bir sıraya göre dizmeye yarar. Türkçe gibi ASCII tablosunda yer almayan karakterler içeren diller için yanlış sıralama yapabilir. Birçok farklı yöntem ile bu fonksiyonun özel karakterleri de düzgün sıralaması iyileşir fakat tamamen düzelmez.

# sorted() fonksiyonu hangi değeri alırsa alsın liste tipinde veri döner.Karakter dizisi şeklinde verilen sayıları dahi sıralayıp liste dönebilir.

sorted("1235464342357") # Output : ['1', '2', '2', '3', '3', '3', '4', '4', '4', '5', '5', '6', '7']


# sum() # -> Bir dizi içerisindeki sayıların toplamını döndürür.

# type() # -> Nesnelerin hangi tipte olduğunu döndürür.

 
# zip() # -> İki listenin öğelerini birbirleriyle eşleştirir. zip nesnesi döner. Listeye çevrilerek kullanılabilir.


isimler = ["Ali","Veli","Ayşe","Kemal"]

yaslar = [12,34,5,7]

for isim,yas in zip(isimler,yaslar):
	print("İsim:",isim,"Yaş:",yas)
	
	

