# Python p117


##### 17. İKİLİ (Binary) DOSYALAR #####

# Dosyalar çoğunlukla iki farklı sınıfa ayrılır:
  
  # Metin Dosyaları : Bir metin düzenleyici ile açıldığında (Örneğin: Notepad) okunabilir formda olan dosyalar metin dosyalarıdır.
  
  # İkili (Binary) Dosyalar : Metin düzenleyicilerle açılamayan, açılmaya çalışıldığında ise çoğu zaman anlamsız karakterler içeren dosya türleri İkili Dosyalardır. Örneğin resim dosyaları, müzik dosyaları, video dosyaları, MS Office dosyaları, LibreOffice dosyaları, vb.


# Bilgisayarlar için sadece İkili Dosyalar(Binary Files) vardır. İçlerinde ne olursa olsun bilgisayarlar tüm dosyaları ikili dosya olarak görür.

# Bir metin dosyasındaki ufak değişiklikler dosyanın okunamaz hale gelmesine yol açmaz. Olabilecek en kötü şey, değiştirilen karakterin okunamamasıdır. Fakat ikili dosyalarda ufak değişiklikler dosyanın tümden bozulmasına yol açabilir.

f = open("python-istihza.pdf","rb")

okunan = f.read(10)

f.close()

# PDF, JPEG, PNG, TIFF, BMP, vs gibi dosya tiplerinin nasıl okunabileceği daha sonra teknik şartnamelerine bakarak incelenecektir.

import csv

with open("FL_insurance_sample.csv") as csv_file:
    sayac=0
    liste=csv.reader(csv_file)
    for item in liste:
        sayac=sayac+1
        if sayac !=1:
            print("PolicyID : {0}\nState Code : {1}\nCounty : {2}\n####################### ".format(item[0],item[1],item[2]))
        if sayac==5:
            break


