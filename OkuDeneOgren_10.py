# Python p110

#### 10.KARAKTER DİZİLERİNİ BİÇİMLENDİRMEK ####


## s Anahtar Harfi 

parola=input("Parola Giriniz: ") # Kullanıcıdan parola bilgisi alındı.

print("Girilen Parola: %s" %parola) # Parola bilgisi ekrana string format yapısı ile yazdırıldı. Burada yer alan 's' anahtar harfi string degerleri ifade eder.


kullanici=input("Kullanıcı Adı: ")
sifre=input("Şifre: ")

print("'%s' kullanıcı adını ve '%s' şifresini kullanarak giriş yapıldı."%(kullanici,sifre)) # s anahtar harfi kullanılarak çoklu değişken ataması yapıldı.

print("Bugün saat %(saat)s civarında %(yer)s mevkisinde onunla görüşeceğiz." %{"saat":15,"yer": "Eminönü"}) 
# Yazılan metni ekrana yazarken 'saat' ve 'yer' değişkenlerini metin sonrasında tanımlanan sözlük yapısından getirdi.

############################################################

## d Anahtar Harfi


yas=input("Doğum Yılınızı Giriniz: ") # Kullanıcıdan doğum yılı bilgisi alındı.

if(yas.isdigit()): # 'yas' adlı değişken sayısal değer olup olmadığını kontrol eder.
    yas=int(yas) # 'yas' değeri integer tipi olarak atanır.
    yas=2018-yas
    print("Yaşınız: %d"%yas) # d anahtar harfi ile sayısal değerler ekrana yazdırıılır.
else:
    print("Lütfen geçerli bir doğum yılı giriniz.")

############################################################

## f Anahtar Harfi

print("Dolar : %f\nEuro : %.4f\nAltın : %f$ "%(5.5011,6.2407,1217.80)) #


############################################################

## format() Metodu


print("""{0} dili oldukça esnek bir yapıdadır.Örneğin {1} teknolojisi ile
web programlama ve {2} kütüphanesiyle birlikte de mobil programlamayı
{0} dilinde yapmak mümkündür.""".format("Python","Django","Kivy"))

############################################################

kalkis= input("Kalkış yeri: ")
varis = input("Varış yeri: ")
isim_soyisim = input("İsim ve Soyisim: ")
bilet_num = input("Bilet Sayısı: ")


# 1.Yöntem

#print("""{0} noktasından {1} noktasına, 14:30 hareket saatli
#sefer için {2} adına {3} adet bilet ayrılmıştır!""".format(kalkis,
#                                                         varis,
#                                                         isim_soyisim,
#                                                         bilet_num))


# 2.Yöntem

ifade="""{0} noktasından {1} noktasına, 14:30 hareket saatli
sefer için {2} adına {3} adet bilet ayrılmıştır!"""

print(ifade.format(kalkis,varis,isim_soyisim,bilet_num))


############################################################


print("{dil} Programlamaya Giriş Dersleri".format(dil="Python")) # 'dil' değişkeni format yapısı kullanılarak içerde tanımlanır ve atanır.


############################################################

## f-string

# f-string yapısı python 3.6 sürümünden sonra gelmiştir. Bu metot yardımıyla
# format metodunu kullanmadan karakter dizileri biçimlendirilebilir.

ad=input("Kullanıcı Adı: ")
sifre2=input("Şifre: ")

print(f"'{ad}' kullanıcı adı ve '{sifre2}' şifresi kullanılarak giriş yapılmıştır.") # 'ad' ve 'sifre2' değişkenlerine atanan değerler ekrana yazdırılır.







