# Python p103 


# Projenin hangi dosya yolunda çalıştığını bilmek için "os" modülünün getcwd() fonksiyonu kullanılabilir.

import os

print(os.getcwd()) # os.getcw() ile alınan dosya yolu print() fonksiyonu ile ekrana yazdırılır.





d=open("denemeDosyasi/kisisel_bilgiler.txt","w")
print("Ahmet Ahmet",file=d)
d.close() # Python close() fonksiyonunu görmeden dosyaya bir şey yazmaz. Dosyaya eklenmek istenen bilgileri Python tampona kaydeder. close() fonksiyonunu görünce tampondaki bilgileri standart çıktı konumuna ekler.



f=open("denemeDosyasi/kisisel_bilgiler_2.txt","w")
print("Python Programlamaya Giriş",file=f,flush=True) # "flush" parametresi başlangıçta yani hiç kullanılmadığı zamanda değeri False'dir. Değeri True olarak atanınca ilgili "f" dosyası close() fonksiyonu kullanılarak kapatılmazsa bile dosyaya print() ile yazdırılan bilgiyi ekler.



print("Python") # print() fonksiyonu içerisine tek parça halinde yazılan karakter dizisi tek parça olarak algılanır.
print(*"Python") # print() fonksiyonu içerisine yıldızlı olarak yazılan karakter dizisinin her elemanını print() fonksiyonuna teker teker gönderir. Tek parametre alan fonksiyonlarda böyle yıldızlı kullanım hata ile sonuçlanır.

# len(*"python") # HATALI KULLANIM!

# print(*1345)  # HATALI KULLANIM! #Yıldızlı parametreler sayılarla birlikte kullanılmazlar!

# print() fonksiyonu içinde kullanılan "file" parametresi ile standart dosya yazma konumu geçici olarak değiştirilebiliyor. Fakat dosya yazma konumu kalıcı olarak değiştirilmek istenirse bunun için sys.stdout komutu kullanılmalıdır.

#import sys #sys modülü import yardımıyla projeye eklendi. import anahtar kelimesi önceden tanımlanmış kullanıma hazır modülleri projeye dahil etmek için kullanılır.


# Standart Çıktı Konumunu Değiştirme
# sys.stdout=f # Standart dosya yazım konumu f adlı önceden oluşturulmuş dosya ile değiştirilir.
# Bundan sonra print() fonksiyonu ile yazılanlar Etkileşimli Kabuk'a yazılmadan f ile tanımlanan dosyanın içerisine yazılır.

#print("Selam Dünya!",flush=True) # Eğer print() fonksiyonunun yazdığı dosya daha önce close() fonksiyonu ile kapatılıp açılmamışsa bu kısımda hata alınır.
#Daha öncesinde açılan bir dosyaya print() fonksiyonu ile bir şeyler yazılmak istenirse "flush" parametresi True konuma getirilir. Dosyaya yazmak için print() dosyanın kapanmasını beklemez ve dolasıyla hata alınmaz.


#print(sys.stdout.name,flush=True) # sys.stdout.name : O an geçerli olan standart dosya yazım yerini verir.

#print(sys.stdout.mode,flush=True) # sys.stdout.mode : standart dosyanın hangi dosya kipi ile açıldığını verir.

#print(sys.stdout.encoding,flush=True) # sys.stdout.encoding : standart dosyasına karakterlerin hangi kodlama biçimi ile yazılacağını verir.



# Standart Çıktı Konumunu Eski (Default) Haline Getirme
import sys
#f=open("kisisel_bilgiler_2.txt","w")

#sys.stdout, f = f, sys.stdout
#f, sys.stdout = sys.stdout, f

#print("deneme")





