# Python p105

#### pass & break & continue ######

while True:
    parola = input("Parola belirleyin: ")

    if not parola:
        pass # pass deyimi "eğer parola değişkeni boş olursa program bu durumu hiç dikkate almadan devam etsin" demektir.

    elif len(parola) in range(3, 8): # Eğer parolanın uzunluğu 3 ile 8 karakter arasında ise bu koşul altına yazılanlar çalışır.
        print("Yeni parolanız", parola)
        break # break deyimi ile döngüden tamamen çıkılır.(while döngüsünden)

    elif len(parola) > 8:
            print("Parola 8 karakterden uzun olmamalı")
            continue # Eğer parolanın karakter sayısı 8 den fazla olursa program bu adımı geçer ve döngünün başından devam eder.
    else:
        print("Geçersiz parola")
        
		
###### Karakter Dizilerinin İçeriklerini Karşılaştırma ######
        
ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

for s in ikinci_metin: # ikinci_metin'deki karakterlerin hepsi tek tek 's' adlı değişkene atılır.
    if not s in ilk_metin: #eğer 's' adlı bu öğe ilk_metin'de yoksa
        print(s) #'s' adlı öğeyi ekrana bas


###### Dosyaların İçeriklerini Karşılaştırma ######

d1 = open("isimler1.txt") # 'isimler1.txt' adlı dosya okuma kipi ile açılır.
d1_satırlar = d1.readlines() #  'isimler1.txt' adlı dosyanın satırları tek tek okunur ve dizi olarak d1_satırlar değişkenine atanır.

d2 = open("isimler2.txt") # 'isimler2.txt' adlı dosya okuma kipi ile açılır.
d2_satırlar = d2.readlines() 

for i in d2_satırlar:
    if not i in d1_satırlar:
        print(i)
        
# Açılan dosyalar kapanır.
d1.close() 
d2.close()


###### Dosyanın İçerisinde Belirtilen Karakterinin Sayısını Bulma ######

hakkında = open("hakkında.txt", encoding="utf-8") # 'hakkında.txt' adlı dosya utf-8 karakter kodlamasıyla açıldı.

harf = input("Sorgulamak istediğiniz harf: ") # Kullanıcıdan sorgulanmak istenen harf alınıp 'harf' adlı değişkene atandı.

sayac = 0 # sayac sıfırlandı.

for karakter_dizisi in hakkında: # hakkında adlı dosya her satır ayrı bir karakter dizisi elemanı olacak şekilde 'karakter_dizisi' adlı diziye atıldı.
    for karakter in karakter_dizisi: # 'karakter_dizisi' adlı satır dizilerinin içine girerek karakterler tek tek 'karakter' adlı değişkene atıldı.
        if harf == karakter: # Dosyada incelenen karakterin aranan harf ile aynı olup olmadığı kontrol edilir.
            sayac += 1 # Eğer aynı aranan harf dosyadan okunan karakter ise sayac 1 arttırılır.
print(sayac) # sayac ekrana yazdırılır.
 
hakkında.close() # Açılmış olan dosya kapatılır.






