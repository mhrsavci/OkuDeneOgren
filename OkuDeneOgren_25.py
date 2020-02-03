# Python p125

#### 23. GÖMÜLÜ FONKSİYONLAR - 3 #####

# filter() # -> Dizi niteliğini taşıyan nesneler içerisinde bir nevi süzme işlemi uygulanabilir.

liste = [1,2,34,53,6,7,8,23,455,35342,5673,5,7,54,78,90,09,67,00,123]

def Cift(s):
	if s%2==0:
		return True
	else:
		return False
		
filter(Cift,liste) # -> Cift() fonksiyonunu "liste" adlı listenin tüm elemanlarına uygular True olanları filter objesi şeklinde döndürür. Bu dönen filter objesi list ile listeye çevirilebilir.

# filter() fonksiyonu liste veya sözlük tipinde verilmiş verileri etiketlemek için kullanılabilir. Örneğin not dağılımı listesinde notlara harflendirme yapmak için kullanılabilir.


# isinstance() # -> Bir nesnenin belirtilen tipte olup olmadığını döner.

isinstance("karakter",str) # Output: True
isinstance("karakter",list) # Output: False

# len() #-> Nesnelerin karakter uzunluklarını hesaplar.

# map() # -> Bir liste elemanları üzerinde toplu bir işlem yapmaya yarar.


liste = [1,2,3,4]

def Carp(sayi):
	return sayi*2

ikikat = list(map(Carp,liste)) # "liste" adı listenin tüm elemanlarına Carp adlı fonksiyon uygulandı.

# max() # -> Liste formunda nesnelerin içerisinden maksimum elemanı döndürür. 

Enbuyuk = max(1,2,3)
Enbuyuk = max([1,2,3])

karakterler = ["elma","armut","mandalina","muz"]

Enuzun = max(karakterler,key=len) # key parametresi ile karakterlerden oluşan listeler içerisinde de en uzun karakteri döner.

######### min() Fonksiyonu Uygulama Örneği #######

def en_yüksek_rütbe(rütbe):
rütbeler = {'er' : 0,
			'onbaşı' : 1,
			'çavuş' : 2,
			'asteğmen' : 3,
			'teğmen' : 4,
			'üsteğmen' : 5,
			'yüzbaşı' : 6,
			'binbaşı' : 7,
			'yarbay' : 8,
			'albay' : 9}
	
	return rütbeler[rütbe]


askerler = {'ahmet': 'onbaşı','mehmet': 'teğmen','ali': 'yüzbaşı','cevat': 'albay','berkay': 'üsteğmen','mahmut': 'binbaşı'}

print(max(askerler.values(),key=en_yüksek_rütbe))

# min() # -> max() foksiyonu gibi çalışır. En düşük değerleri bulur.

## open() fonksiyonu :
# open() # -> open() fonksiyonu dosya açma işlemlerinde kullanılır.

# open() fonksiyonunun aldığı parametreler: 

# open(dosya_adi, mode='r', buffering=-1, encoding=None, errors=None,  newline=None, closefd=True, opener=None)

# Karakter Anlamı (mode parametresiyle birlikte kullanılan dosya açma kipleri. mode yazılmadan da kullanılabilir.)
# ------------------
# ‘r’ : Okuma kipidir. Öntanımlı deger budur.
# ‘w’ : Yazma kipidir. Eger belirtilen adda dosya zaten varsa o dosya silinir.
# ‘x’ : Yeni bir dosya olusturulup yazma kipinde açılır.
# ‘a’ : Dosya ekleme kipinde açılır. Bu kip ile, varolan bir dosyanın sonuna eklemeler yapılabilir.
# ‘b’ : Dosyaları ikili kipte açmak için kullanılır.
# ‘t’ : Dosyaları metin kipinde açmak için kullanılır. Öntanımlı degerdir.
# ‘+’ : Aynı dosya üzerinde hem okuma hem de yazma islemleri yapılmasını saglar.

# f = open(dosya.txt,"a+")

# open() fonksiyonuyla bir dosyayı açıp bu dosyaya veri girildiğinde bu veriler önce tampona alınacak, dosya kapandıktan sonra ise tamponda bekletilen veriler dosyaya işlenecektir. buffering parametresi yardımıyla bu tampona alma işleminin nasıl yürüyeceği belirlenebilir. Eğer dosyaya işlenecek verilerin tampona alınmadan doğrudan dosyaya işlenmesi istenirse buffering değerini 0 olarak belirlenebilir. Yalnız bu deger sadece ikili kipte etkindir. Yani bir dosya metin kipinde açılırsa buffering parametresinin degeri 0 olamaz. Eğer dosyaya veri işlerken tampona alınan verilerin satır satır dosyaya eklenmesi istenirse buffering değeri 1 olarak belirlenebilir. buffering parametresinin 1 değeri sadece metin olarak açılan dosyalarda kullanılabilir.0 ve 1 dısında buffering parametresine 1’den büyük bir değer verildiğinde ise tampon boyutunun ne kadar olacağı kullanıcı tarafından belirlenebilir.

# f = open('ni.txt', 'w', buffering=1)

# open() fonksiyonu ile kullanılan bir diğer parametre encoding parametresidir. encoding parametresi karakter kodlamasını belirlemek için kullanılır. Bu parametrenin hangi değeri alacağı önemlidir. Çünkü dosya uygun olmayan karakter kodlaması değerleriyle açılamaz.

# f = open('dosya.txt', encoding='utf-8')

# Bir dosyayı açarken veya okurken herhangi bir karakter kodlama hatası ile karşılaşıldığında Python’ın ne tepki vermesi gerektiğini ise errors adlı parametre yardımıyla belirlenebilir. Eğer bu parametreye "strict" değeri verilirse karakter kodlama hataları programın "ValueError" türünde bir hata vererek çalışmayı kesmesine neden olacaktır. Bu parametreye herhangi bir değer verilmediğinde de Python sanki strict degerini verilmiş gibi davranır. Eğer errors parametresine "ignore" değeri verilirse kodlama hataları görmezden gelinecek, bu hataya sebep olan karakter(ler) silinecektir. Yalnız bu değerin veri kaybına yol açma ihtimali de göz önünde bulundurulmalıdır. Eğer errors parametresine "replace" değeri verilirse kodlama hatasına yol açan karater ‘?’ veya ‘ufffd’ karakterleri ile değiştirilecektir.

# f = open('dosya', newline='\n') # -> Bu şekilde dosya hangi işletim sisteminde olursa olsun satır sonlarında "\n" karakterine sahip olacaktır.

# fileno() fonksiyon bir dosyanın ‘dosya tanımlayıcısını’ (file descriptor ) verir. Dosya tanımlayıcıları, dosyaya işaret eden pozitif tam sayılardır. 0, 1 ve 2 sayıları standart girdi, standart çıktı ve standart hata dosyalarına ayrılmıs oldugu için, sonradan açılan ve üzerinde işlem yapılan dosyaların tanımlayıcıları 2 sayısından büyük olacaktır.Her dosyanın dosya tanımlayıcısı benzersizdir.

g = open('zi.txt')
g.fileno() # Output: 4

a  = open("aaa.txt")
b = open("bbb.txt")

c = open(b.fileno(),closefd=False) # Normalde bir dosya açılıp kapandığında dosya tanımlayıcısı serbest kalır. Fakat closefd parametresi False olursa açılan dosya kapansa bile dosya tanımlayıcısı serbest kalmaz.

















