# Python p127

#### 24. İLERİ DÜZEY FONKSİYONLAR #####


# LAMBDA FONKSİYONLARI
-----------------------

# Tanımlanması : fonksiyon_adi = lambda parametre1,parametre2 : parametre1 ve parametre2 ile yapılacak işlem.
# Çağırılması : fonksiyon_adi(parametre1,parametre2)

TekMi = lambda x:x%2!=0 

TekMi(12)
Tekmi(15)

# RECURSIVE FONKSİYONLAR
--------------------------

# Fonksiyonun kendi içerisinde yine kendisinin çağırıldığı fonksiyon türleridir.

# Verilen bir karakter dizisini tersten yazan Rekursif Fonksiyon örneği:

def Hecele(kelime):
    if len(kelime)>0:
        print(kelime[-1])
        kelime = kelime[0:(len(kelime)-1)]
        return Hecele(kelime)
		




	
	
	