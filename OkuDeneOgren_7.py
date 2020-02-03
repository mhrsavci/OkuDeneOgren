# Python p107

### 7. Karakter Dizileri ###

karakter = "Python Programlamaya Giriş"

print(karakter[0:6]) # 'karakter' adlı karakter dizisinin 0.indeksli elemanından başlar 6 eleman getirir.

print(karakter[::-1]) # 'karakter' adlı diziyi ters çevirir.

print(karakter[::]) # 'karakter' adlı dizinin tüm karakterlerini getirir.

print(karakter[7:]) # 'karakter' adlı dizide 7.indeksten dizinin sonuna kadar getirir.

print(karakter.replace("P","C")) # 'karakter' adlı karakter dizisinde bulunan 'P' karakterlerini 'C' karakterine çevirir.

print(karakter.split()) # 'karakter' adlı diziyi boşluk karakterine göre parçalara ayırıp parçaları başka bir diziye atar.

import locale
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") # Türkçe karakterleri doğru sıralamak için böyle bir ayar eklendi.
print(sorted(karakter,key=locale.strxfrm)) # 'karakter' adlı dizinin elemanlarını sıralar.

harfler = "abcçdefgğhıijklmnoöprsştuüvyz" # Alfabede bulunan tüm harfler yazıldı.
cevrim = {i: harfler.index(i) for i in harfler} # for döngüsü ile harfler değişkeninde dönülüp tüm elemanlara bir sayı atandı.
sorted("afgdhkıi", key=cevrim.get)

# Üç Önemli Fonksiyon : dir - help - enumerate

# dir() : Python' da bulunan herhangi bir obje hakkındaki bilgileri döndürür.
# help() : Python' da bulunan herhangi bir objenin dokümantasyon bilgisini döndürür.
# enumerate() : Değer olarak aldığı bir karakter dizisinin elemanlarını sıralı numaralara atar. Döngüsel değer döndüğü için for döngüsüyle içeriği yazılabilir.

 
