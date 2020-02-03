# Python p102


#### 4.print() Fonksiyonu ####

# print() fonksiyonunun görevi karakter dizilerini ekrana çıktı olarak yansıtmaktır. Etkileşimli kabukta çalışırken ekrana çıktı vermek için print() fonksiyonunu kullanmak gerekmez.

#      fakat bir başka dosyada yazılı olan python kodlarını çalıştırarak ekrana bir şey yazılmak istenirse mutlaka print() veya benzeri fonksiyonlar kullanmak gerekir.

# print() fonksiyonu içerisine karakter dizileri yazılırken tırnak işareti kullanılmalıdır. Python içerisinde kullanılan üç farklı tırnak işareti vardır:

## Tek Tırnak (' ')
## Çift Tırnak (" ")
## Üç Çift Tırnak (""" """)

print("Programlama Dili : 'Python' ") # Eğer ekrana yazdırılacak olan ifade içerisinde tek tırnak varsa ifade print() fonksiyonu içerisinde ya çift ya da üç çift tırnak arasına yazılmalıdır.

print('Programlama Dili : "Python"') # Eğer ifade içerisinde çift tırnak kullanımı varsa ifade print() fonksiyonu içerisinde  ya tek ya da üç çift tırnak arasına yazılmalıdır.

# Üç Çift Tırnak içerisine her türlü karakter yazılabilir. Üç Çift Tırnak arasına yazılan ifadeler peş peşe eklenmeden nasıl paragraf formatında yazıldıysa o şekilde ekrana yansıtılır. Karakterlerin yazım formatları bozulmaz.

print("""Selamlar,


Python kolay öğrenilebilen bir programlama dilidir.



Saygılarımla.
""")


print("Python","Programlamaya","Giriş","Serisi") # print() fonksiyonu içerisine ard arda yazılan karakter dizilerini birbirlerine ekleyip ekrana tek parça şeklinde yazabilir.


print("Python","Programlamaya","Giriş","Serisi","7",sep="_") # print() fonksiyonu içerisine yazılan karakter dizileri "sep" parametresi ile birlikte verilen karakterle araları ayrılabilir. "sep" parametresi ile karakter dizilerinin aralarına yerleştirilecek olan karakter belirlenir.

print("Python","Programlamaya","Giriş","Serisi",end=".") # print() fonksiyonu içerisine yazılan karakter dizilesinin sonuna eklenecek karakter "end" parametresi ile belirlenebilir.


# print() fonksiyonunun "sep" ve "end" parametrelerinden sonra aldığı bir diğer önemli parametre de "file" dır. print() fonksiyonu eğer ek bir ayar yapılmadı ise içerisine yazılan
#    karakter dizisini Etkileşimli Kabuğa yazar. "file" parametresi ile print() fonksiyonunun içerisindeki değeri nereye yazacağı belirlenir. "file" parametresinin ön tanımlı değeri "sys.stdout" tur. "sys.stdout"
#    'standart çıktı konumu' demektir. Standart çıktı konumu print() fonksiyonun çıktılarını yazdığı konumdur. Örneğin Python ön tanımlı olarak, ürettigi çıktıları ekrana verir. Eğer o anda Etkilesimli Kabukta
#    çalışılıyorsa, Python ürettigi çıktıları Etkileşimli Kabuk üzerinde gösterir. Eğer yazılan bir programı komut satırında çalışıyorsa, üretilen çıktılar komut satırında görünür.
#    Dolayısıyla Python’ın standart çıktı konumu Etkileşimli Kabuk veya komut satırıdır.

import sys # sys adlı kütüphane projeye dahil edildi. import öneki ile hazır modüller projeye dahil edilebilir ve [modül adı].[fonksiyon adı] şeklinde modül içerisinde yer alan fonksiyonlar kullanılabilir.
print("Selam Dünya!",file=sys.stdout) # Karakter dizisi print() fonksiyonunun standart çıktı konumuna yazıldı yani Etkileşimli Kabuğa.


dosya = open(r"C:\Users\mhr\Desktop\OkuDeneOgren\denemeDosyasi\deneme_2.txt","w") # open() fonksiyonu gösterilen dizinde istenilen isimde bir dosya oluşturur. "w" anahtar harfiyle dosyayı write yetkisiyle açar.
# Eğer gösterilen konumda dosya yoksa oluşturur varsa var olan dosyanın içeriğini temizler.
#Oluşturulan dosya "dosya" adlı değişkene atanır. Bundan sonra oluşturulan dosya ile ilgili işlemlerde "dosya" değişkeni kullanılır.
# open() fonksiyonunun içerisinde yazan 'r' harfi ile / işaretlerinden dolayı oluşacak özel karakterlerin çalışmasının önüne geçilmiş olur.

print("Merhaba, ben Python' dan geliyorum!", file=dosya) # print içerisine yazılan karakter dizisi "file" parametresiyle gösterilen konuma yazılır.
dosya.close() # "dosya" adında oluşturulan dosya kapatılır. Eğer açılan dosyalar kapatılmazsa program hata verir. Mutlaka kapatılmalıdır!



   



