# Python p115

#### 15. TEMEL DOSYA İŞLEMLERİ #####

f=open("deneme.txt","w") # deneme.txt adlı bir dosya yazma kipi ile oluşturuldu.
# Eğer deneme.txt adlı bir dosya varsa var olan dosyanın içerisini temizler.


f.write("Deneme123") # f adlı açılan/oluşturulan dosya içerisine yazım işlemi yapıldı.

f.close() # f adlı dosya kapatıldı.


f=open("deneme.txt","r") # deneme.txt adlı dosyayı okumak için açar.
# Eğer deneme.txt adlı bir dosya yoksa hata verir.



#d = open("fihrist.txt","w")

#d.write("""Ahmet Özbudak : 0533 123 23 34
#Mehmet Sülün  : 0532 212 22 22
#Sami Sam      : 0542 333 34 34 """)

#print(d.read())

#d.close()

d = open("fihrist.txt","r")

#print(d.read()) # Dosya içerisinde tüm yazılı olan ifadeyi ekrana basar.

print(d.readline()) # Dosya içerisinin ilk satırını getirir.

print(d.readlines()) # Dosya içerisini listeye atılmış hali ekrana basıldı.

d.close()

# Bir dosyayıyı read(), readline() veya readlines() metotlarından herhangi biri ile okunduğunda imleç başa dönmez.


# d.seek(10) # Dosya içerisinde bulunan okuma imlecini 10.indekse konumlandırır.
# d.tell() # O anda dosya içerisindeki okuma imleci hangi konumda ise o konum döner.


#with open("test.txt","r+") as dosya: # Eğer dosya yoksa oluşturmaz. r+ kipi ile dosya hem okumak hem de yazmak için açılır.
#    liste=dosya.read()
#    dosya.write("Test deneme amaçlı oluşturulan dosya")

with open("test.txt","w+") as file: #Dosya hem okumak hem yazmak için açılır. Eğer dosya varsa içeriği temizlenir. Dosya yoksa yeniden oluşturulur.
    file.write("Test amaçlı oluşturulan dosya")
    liste = file.read()
    print("liste")

file=open("testtest.txt","a") # Dosya yazma kipi ile açılır. Dosya mevcut değilse oluşturulur eğer belirtilen isimde bir dosya varsa dosyanın içeriğinde herhangi bir silme yapılmaz.




