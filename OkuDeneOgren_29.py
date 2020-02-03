# Python p129


#### 26. OOP (OBJECT ORIENTED PROGRAMMING) NESNE TABANLI PROGRAMLAMA - 1 #####

# Nesne Tabanlı Programlama bir programlama yaklaşımıdır.
# Nesne tabanlı programlamanın temelinde adından da anlaşılacağı üzere "nesne" yer almaktadır.
# class yapıları Python programlama dilinde nesne üretmek için kullanılan bir yapıdır.

# Scobe(Etki alanı):

def FonksiyonAdi():
	# Burası 'FonksiyonAdi' adlı fonksiyonunun Etki Alanı'dır.
	
# Etki alanı dışında bulunan değişkenleri değiştirebilmek için değişkenleri etki alanlarına "global" anahtar kelimesiyle yazmak gerekir. 
# Sadece görüntülemek, değer almak için kullanılırsa "global" anahtar kelimesiyle tanımlanmasına gerek yoktur. 
# Örneğin:

########################################################
sayac = 0


def artir():
	global sayac
	
	sayac += 1
	
	return sayac
	
	
def goster():
	return sayac
	

def azalt():
	sayac = sayac-1 # Hata verir,  böyle bir değişken tanımadığını söyler çünkü sayac değişkeni global anahtar kelimesiyle etki 
	# alanı içerisine dahil edilmedi.
	
	return sayac 
########################################################


# Bir sınıftan nesne oluşturmak için sınıftan instance alınır. Yani o sınıftan örnek oluşturulur. Örneğin Personel isimli bir class' tan 
# örnek oluşturmak için: 

personel = Personel() # Buradaki personel örneğinin adı Personel() sınıfının tüm özelliklerini taşır.


# __init__() fonksiyonu : Bir sınıftan instance oluşturulduğunda yapılacak işler bu fonksiyon içerisine yazılır. Bir nevi 
# constructor - yapıcı(kurucu) fonksiyondur.

class Personel():
	
	def __init__():
		print("Sınıftan örnek oluşturuldu.")

# Sınıftan örnek olarak oluşturulan nesnelere özel özellikler sınıf içerisinde "self" anahtarı ile oluşturulur. "self" anahtar kelimesi, 
# içinde kullanılacağı fonksiyonun ilk parametre ismi olarak tanınır. Yani hangi fonksiyon içerisinde kullanılırsa o fonksiyonunun 
# ilk parametresi self olmak zorundadır.

# Sınıf nitelikleri sınıf içerisinde fonksiyonların dışarısında tanımlanır.

# Bir örnek için tanımlanacak özellik sadece sınıf içerisindeki fonksiyonların içerisinde tanımlanabilir. 
# Fonksiyonların dışında bir örnek niteliği tanımlanamaz.


# Sadece sınıfın kendisine has bir fonksiyon tanımlamak için fonksiyonu tanımlarken bir üst satırına "@classmethod" yazılır. 
# Sınıfın öğelerine "self" ile değil "cls" ile erişilir.


class Makina():

	MakinaListesi=[]
	
	def __init__(self,makina_Adi):
		MakinaListesi.append(self.makina_Adi)
		print("Örnek oluşturuldu.")
		
	@classmethod
	def MakinaSayisi(cls):
		print(len(cls.MakinaListesi))



# Python' da "@" işaretiyle kullanılan öğelere "decorator" denir.
 
 
# Statik metotlar hem örnek adları üzerinden hem de sınıf adları üzerinden kullanılabilen sınıf içerisinde tanımlanan metotlardır. 
# İşlevsellik açısından statik metotlar ile sınıf metotları aynıdır. Fakat sınıf metotlarında "cls" anahtar parametresi kullanılırken statik metotlarda böyle bir parametre adı kullanılmaz.

# Statik metotlar herhangi bir örnek veya sınıf öğeleri üzerinde işlem yapmazlar. Bu nedenler sınıf içerisinde yer alan bir 
# fonksiyon hem örnek hem de sınıf öğeleri için bir işlem yapmayacaksa statik metot olarak tanımlanabilir.

# Bir sınıf içerisinde örnek özelliklerine "self" parametresi ile sınıf özelliklerine "cls" parametresi ile erişilir. 
# Bu parametreler hangi fonksiyon içerisinde kullanılacaksa o fonksiyonun ilk parametresi olarak yazılmalıdır. Bir fonksiyonun ilk parametresi self veya cls olarak tanımlanmasa bile fonksiyon o parametrelere self veya cls gibi davranır. self veya cls yazılması tamamen Python kod düzeni için kabul görmüş bir davranıştır. 







	
