# Python p118

###### 18. SÖZLÜKLER #######


kelimeler={"kitap":"book","defter":"notebook"}

print(kelimeler["kitap"]) #Output: book


## SozlukAdı={"anahtar":"deger","anahtar":"deger",...}


kişiler = {"Ahmet Özkoparan": {"Memleket": "İstanbul",
                               "Meslek"  : "Öğretmen",
                               "Yaş"     : 34},

           "Mehmet Yağız"   : {"Memleket": "Adana",
                               "Meslek"  : "Mühendis",
                               "Yaş"     : 40},

           "Seda Bayrak"    : {"Memleket": "İskenderun",
                               "Meslek"  : "Doktor",
                               "Yaş"     : 30}}



isim = "Hakkında ayrıntılı bilgi edinmek \
istediğiniz kişinin adını girin: "

arama = input(isim)

ayrinti = input("Memleket/Meslek/Yaş? ")

print(kişiler[arama][ayrinti])


personel = {"Mehmet Öz": "AR-GE Müdürü","Samet Söz": "Genel Direktör","Sedat Gün": "Proje Müdürü"}


## Sözlüklere eleman eklemek.

personel["Melih Balta"]="Mühendis"


# Sözlükler değer olarak her türlü veri tipini kabul eder fakat anahtarları açısından böyle değildir. Yani sözlüklere anahtar olarak her veri tipi atanamaz. Bir değerin ‘anahtar’ olabilmesi için, o öğenin değiştirilemeyen (immutable) bir veri tipi olması gerekir.

#Python’da şimdiye kadar öğrenilen şu veri tipleri değiştirilemeyen veri tipleridir:
# 1. Demetler
# 2. Sayılar
# 3. Karakter Dizileri

Dolayısıyla sadece Demetler, Sayılar ve Karakter Dizileri anahtar olarak sözlüklere eklenebilir.

##Şu veri tipleri ise değiştirilebilen veri tipleridir:

# 1. Listeler
# 2. Sözlükler


### 19. SÖZLÜK METOTLARI ####


szlk={"a":1,"b":2,"c":3,"d":4,"e":5}

print(szlk.keys()) # szlk adlı sözlük içerisinde bulunan elemanların anahtar ifadelerini döndürür.

print(szlk.values()) # szlk adlı sözlük içerisinde bulanan elemanların değer ifadelerini döndürür.

print(szlk.items()) # szlk adlı sözlük içerisinde bulunan elemanları anahtar-değer yapısıyla döndürür.

sorgu=input("Lütfen sırasını öğrenmek istediğiniz harfi giriniz: ")

print(szlk.get(sorgu,"Aranan harf sözlükte yer almamaktadır.")) # Eğer sözlük içerisinde aranan değer yoksa uyarı mesajı döndürülür.

# print(szlk.clear()) # szlk sözlüğünün içerisi tamamen temizlenir.

sozluk=szlk # Var olan liste veya sözlük tipini başka bir değere atamak demek kopyalamak değil bellekteki aynı nesneye gönderme yapan iki farklı isim belirlemekten ibarettir. "szlk" ifadesinde yapılan bir değişiklik "sozluk" ifadesini de etkiler. Bu nedenle listeyi veya sözlüğü kopyalamak için copy() metodu kullanılmalıdır.


sozluk=szlk.copy()


siralar="0","1","2","3","4","5"

degerler=dict.fromkeys(siralar,"Deger") # Anahtarları "siralar" dan değerleri de "Deger" ifadesinden oluşan sözlük tanımlandı.

print(degerler) 


sozluk.pop("a") # "sozluk" adlı sözlükte bulunan "a" değerini siler. pop() sözlüklerde kullanıldığında mutlaka parametre almaktadır. Sözlükte hangi değer silinecekse pop() metoduna o değer belirtilir. Sözlükte yer alan elemanların anahtar değerlerine göre silme işlemi gerçekleşir.

mesaj=sozluk.pop("z","Silinecek olan değer sözlükte yer almamaktadır.")  # Eğer "z" ifadesini sözlükte bulamaz ise ilgili mesajı ekrana basar.

print(mesaj)

# szlk.popitem() # szlk adlı sözlükten rastgele değer siler, sildiği değeri ekrana yazar.

## Sözlük Üreteçleri 

isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]

isozluk={i:len(i) for i in isimler}

