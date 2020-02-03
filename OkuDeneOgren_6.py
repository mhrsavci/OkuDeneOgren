# Python p106

###### 6. Hata Yönetimi ########

# Programlamada hatayı yönetmek için hatayı yakalamak gerekir. Python' da hatalar 'try-except-finally' anahtar kelimeleri ile yakalanır.

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try: # try bloku içerisine yazılan kodlarda eğer 'ValueError' hatası oluşursa program except blokunu çalıştırır.
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError:
    print("Lütfen sadece sayı girin!")


####################################################

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try: # try bloku içerisine yazılan kodlarda eğer 'ZeroDivisionError' hatası oluşursa program except blokunu çalıştırır.
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")

####################################################

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz!")
except ValueError:
    print("Lütfen sadece sayı girin!")

    
####################################################

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except (ValueError, ZeroDivisionError):
    print("Bir hata oluştu!")
    
####################################################

ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError as hata: # ValueError hatasının açıklaması 'hata' adlı değişkene atandı.
    print(hata)
    
####################################################
    
ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
    
except: # except eğer boş kullanılırsa try bloku içerisine yazılan kodlarda oluşabilecek her türlü hata durumunda çalışabileceğini belirtir.
    print(hata)

finally: # try bloku içerisine yazılan kodlar ister hata versin ister vermesin bu kısım çalışır.
    print("İşlem tamamlandı.")

####################################################

bölünen = int(input("bölünecek sayı: "))

if bölünen == 23:
    raise Exception("Bu programda 23 sayısını görmek istemiyorum!") # Eğer 23 sayısı girilirse ekrana hata yansıtılır ve programdan çıkılır.
#raise komutu ile bir özel Exception tipinde hata oluşturuldu.
bölen = int(input("bölen sayı: "))
print(bölünen/bölen)

####################################################

tr_karakter = "şçğüöıİ"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise TypeError("Parolada Türkçe karakter kullanılamaz!") # Eğer çıkabilecek hata biliniyorsa daha özel hata isimleriyle de hata tanımlanabilir. Sadece Python üzerinde tanımlı hata tiplerine hata atanabilir.    
    else:
        pass

print("Parola kabul edildi!")


