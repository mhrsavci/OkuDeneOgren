# Python p128


#### 25. MODÜLLER #####


# Modül : İçerisinde belli bir amaca yönelik fonksiyonlar barındıran, Python projelerine tekrar tekrar eklenip kullanılabilen hazır kütüphane benzeri yapılara "modül" denir.

# Bir fonksiyon tanımlandığı proje dosyasında tekrar tekrar kullanılabilir. Bir modül de farklı projeler içerisinde projeye dahil edilip tekrar tekrar kullanılabilir. "Modül & Fonksiyon Sistemi" Python içerisinde bir yazılan kodun birden fazla yazılmasını önleyen, uzun kod satırlarından kısa ve sade kod satırlarına geçilmesini sağlayan en önemli düzenleme sistemidir.

# Modüller en basit tabirle fonksiyon kitaplarından oluşan bir kütüphanedir. Modül herhangi bir Python kütüphanesine dahil edilerek içerisindeki fonksiyonlara erişilip kullanılabilir.

# Python içerisinde bir hazır modüller vardır bunlar Python dilini tasarlayan geliştiriciler tarafından oluşturulmuş built-in modüllerdir. Bir de kullanıcılar tarafından çeşitli amaçlarla yazılan kullanıcı tanımlı modüller bulunur. 

# Bir modül(kütüphane) Python projesine çeşitli yollarla dahil edilebilir:

	-> import kütüphane_adi # Kütüphane projeye dahil edildi.
	
	-> import kütüphane_adi as Takma_adi # Kütüphane takma bir isimle(proje içerisinde kullanılabilecek kısaltma bir isim) dahil edildi.
	
	-> from kütüphane_adi import kütüphane_nesnesi # Bir kütüphane içerisinden sadece belirli bir nitelik kullanılacak ise sadece ilgili kütüphane niteliği projeye dahil edilir.
	
	-> from kütüphane_adi import kütüphane_nesnesi1, kütüphane_nesnesi2, ...
	
	-> from kütüphane_adi import kütüphane_nesnesi as takma_nesne_adi
	
	-> from kütüphane_adi import * # Bu şekilde bir modül içindeki bütün fonksiyon ve nitelikleri içe aktarılır.(Modül içerisinde ismi _ ile başlayanlar nesneler hariç)
	

# Modül içeri aktarıldıktan sonra dir(modül_adi) veya dir(modül_takma_adi) fonksiyonu modülün içerisinde yer alan nesneleri döndürür.


# "__file__" nesnesi tüm hazır modüllerde bulunur ve modülün kaynak dosyasını, modülün nerede kurulu olduğunu döndürür.

import os
print(os.__file__)


# Python içerisinde tanımlı modüller Python projesinin çalıştığı her yerde projenin içerisine "import" anahtar kelimesiyle aktarılabilir. Ancak sonradan kullanıcı tarafından tanımlanan modülleri projenin içerisine aktarabilmek için o modül dosyasının Python projesinin çalıştığı yerde yer alması gerekir.


# Bir modül içeri aktarılırken Python iki yere bakar: Python proje dosyasının çalıştığı dizine ve sys.path listesinin içerisine. (sys modülü import sys olarak projeye dahil edilir) sys.path ifadesi bir liste döner ve bu liste dosya yollarından oluşur. Python gider bu dosya yollarını kontrol ederek ilgili modülün orada olup olmadığına bakar. sys.path listesine dosya yolu eklenen modül dosyası diğer önceden tanımlı kütüphaneler gibi Python projesinin çalıştığı her yerden proje içerisine dahil edilebilir. Eğer bu iki yerde içeriye aktarılmak istenen modül hakkında dosya bulamaz ise Python modülü import edemez, hata verir. 

# Yaygın kullanılan durum ise Python kurulum dizini içerisindeki ..\Lib\site-packages dosya yoluna içerisine içeri aktarılmak istenen modülün dosyasının konulmasıdır. Bu dosya yoluna şu şekilde ulaşılır(Bazen çalışmayabilir):

from distutils import sysconfig

print(sysconfig.get_python_lib()) # Burada çıktı olarak döndürülen ..\Lib\site-packages dosya yoludur.


# Python bir modülü içeri aktarırken sys.path içerisindeki dizinleri ararken dizin adlarını sys.path içerisinde soldan sağa doğru okur. [path1, path2, ..., pathn] şeklinde sys.path ile dönen bir liste var olsun. Eğer ilgili modül hem path1 hem de path2 de bulunuyor ise Python path1 de bulunan dosyayı aktarır. path2 deki aktarılmak istenirse liste elemanlarının sırası değiştirilmelidir.(path1 ile path2 nin sırası değiştirilmelidir.)


# Python projesine bir modül eklendiğinde(import edildiğinde) modül dosyası içerisinde değişiklik yapılırsa değişikliğin Python projesine yansıması için modül tekrardan projeye import edilmelidir.

# Python içerisine dışardan, üçüncü şahıs(lar) tarafından tasarlanmış bir kütüphaneyi yüklemek için önce o kütüphanenin dosyalarını indirmek gereklidir. Bunun için "pip" paket yönetimi kütüphanesi kullanılır.

# Eğer bir modül yıldız parametre ile içeri aktarılıyorsa yani "from modül_adi import * " şeklinde Python programına aktarılan modüllerin içerisinde yer alan __all__=[] şeklinde tanımlanan liste içerisinde bulunan modül nitelikleri içeri aktarılabilir. Eğer __all__ listesinde yer almayan bir nitelik varsa "from modül_adi import * " ifadesiyle içeri aktarılamaz. Fakat diğer aktarma yöntemleriyle __all__ listesi içerisinde yer almasa dahi bir nitelik içeri aktarılabilir.

# {'__doc__', '__loader__', '__name__', '__spec__'} nitelikleri sık karşılaşılan niteliklerdir ve tüm Python içindeki modüllerde ve üçüncü şahıslar tarafından yapılan neredeyse tüm modüllerin içerisinde bulunurlar.

# __doc__  : Bu nitelik modül içerisinde bulunan docstring' leri döndürür. donstring'ler (''' ''') veya (""" """) üç tırnaklar arasında yazılan modülün dokümantasyonudur. Eğer (" ") iki tırnak veya ('') tek tırnak içerisine yazılmış dokümante edilmiş bilgi varsa __doc__ niteliği sadece ilk elemanı döndürür.

# __name__ : Bu nitelik iki farklı değer alabilir : İçinde bulunduğu modül adı veya "__main__" adlı özel bir değer. Eğer __name__ niteliğinin modülü herhangi bir modül içerisine dahil edilirse __name__ niteliği kendi modülünün adını alır. Eğer bir modül bağımsız bir Python programı halinde kendi başına çalıştırılıyorsa __name__ niteliği "__main__" adını alır.

# __spec__ : Bu nitelik modüller hakkında çeşitli özellikler barındırır.

import os

print(os.__spec__.name) # Modülün adını getirir.

print(os.__spec__.origin) # Modülün kurulu konumunu getirir.

# __import__("modül_adi") -> Herhangi bir modül satır arasına bu şekilde dahil edilebilir. 
# np = __import__("numpy") -> numpy modülü dahil edildi ve np nesnesine atandı.

