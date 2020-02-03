# Python p120


###### 20. KULLANICIDAN BİLGİ ALMAK ######

# input() fonksiyonu yardımıyla kullanıcıdan bilgi almak mümkündür.


# input() # Kullanıcıdan bir aksiyon beklenir. Eğer kullanıcı bir karakter girerse program çalışmasını keser.

# isim=input("İsminizi Giriniz: ") # input içerisine yazılan mesaj ile kullanıcı bilgilendirildi ve input ile alınan kullanıcı bilgisi 'isim' adlı değişkene atandı.

# print(isim) # input fonksiyonundan dönen değer her zaman karakter dizisidir.

# sayi1=input("Sayi1 : ") # Kullanıcı tarafından sayi1 adlı değişken girildi.
# sayi2=input("Sayi2 : ") # Kullanıcı tarafından sayi2 adlı değişken girildi.

# top=int(sayi1) + int(sayi2) # Girilen sayi1 ve sayi2 değişkenleri integer tipinde veriye dönüştürüldü.

# print(top) 

# str() # Girilen değerlerin tipilerini karakter dizilerini dönüştürür.

# tipi float olan bir sayı ile tipi integer olan bir sayı toplanırsa sonuç float çıkar.
# float() # Tamsayıları veya sayı değerli karakter dizilerini noktalı sayılara dönüştürür.

# print(float(12))

# complex() # Bir sayıyı karmaşık sayıya çevirmek için kullanılabilir.

# print(complex(12))



###### Koşullu Yapılar ######

# Eğer kıyasa dayalı, bir şeyin gerçekleşmesi için başka bir şeyin gerçekleşmesi bağlı ise böyle durumlarda koşul ifadeleri kullanılabilir. En bilindik koşul if-else yapısıdır. if yapısında koşul belirtilir eğer koşul sağlanırsa if bloku içerisine yazılanlar çalıştırılır. Eğer if koşulu gerçekleşmezse else bloku içerisine yazılanlar gerçekleştirilir. if-else yapısına ek olarak bir başka koşul kontrol edilmek istendiğinde if gibi çalışan "elif" ifadesi if-else yapısına eklenir.

import sys #sys adlı modül programa dahil edildi.
while(True): # Program parçacığının sürekli çalışabilmesi için while döngüsü kullanıldı.
    sayi=input("Bir sayı giriniz : ") # Kullanıcıdan bir sayı tahmin etmesi istendi ve kullanıcı tarafından girilen sayi "sayi" adlı değişkene atandı.

    if int(sayi)>17: # "sayi" adlı değişkenin tipi karakter dizisi olduğundan değişkenin tipi integer olarak değiştirildi ve eğer 17 sayısından büyükse if blokunun içerisinin çalıştırılacağı belirtildi.
        print("Lütfen daha küçük bir tahmin yapınız.")
#        if şartı gerçekleştiğinde burası çalıştırılır.
    elif int(sayi)<17: # "sayi" değişkeni 17' den küçükse bu blok çalışır.
        print("Lütfen daha büyük bir tahmin yapınız.")

    elif int(sayi)==17:
        print("Tebrikler! Bildiniz!")
        sys.exit()
    else: # if ve elif ile belirtilen koşullar sağlanmıyorsa else bloku çalıştırılır.
        print("Lütfen uygun bir değer giriniz")


# elif anahtar kelimesi de else anahtar kelimesi de if olmadan tek başlarında çalışamazlar. if tek başına kullanılabilir. if - elif yapısı da else olmadan tek başlarına kullanılabilir. if - else yapısı da elif olmadan tek başına kullanılabilir.