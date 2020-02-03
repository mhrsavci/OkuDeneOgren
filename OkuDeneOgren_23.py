# Python p123

#### 23. GÖMÜLÜ FONKSİYONLAR #####

# abs() -> Mutlak değer fonksiyonudur.

# round() -> Yuvarlama fonksiyonudur

######### round(22/7,2) # : 22/7 sayısını 2. basamağa göre yuvarlar.

# ascii() -> Bir nesnenin ekrana basılabilir halini verir. Eğer ascii kodlamasıyla ekrana basılamıyorsa karakterin UNICODE karşılığını döndürür.

# repr() -> Bir nesnenin ekrana basılabilir halini döndürür. Karakter ascii tablosunda olmasa dahi karakteri ekrana döndürür.

# bool -> Bir nesnenin boolean değerini döndürür.

## bytes ##

# bytes() -> Bir değeri bytes değerine döndürür. Eğer tam sayı verilirse tam sayı kadar bytes nesnesi verir. Bu fonksiyona karakter dizileri doğrudan parametre olarak verilemez. Bir karakter dizisi baytes değerini dönüştürülürken hangi karakter çözücü ile yapılacağı belirtilmelidir.

# bytes("karakter dizisi",encoding="utf-8") ya da bytes("karakter dizisi","utf-8") olarak kullanılabilir.

# bytes("karakter dizisi", encoding="utf-8") == "karakter dizisi".encode("utf-8") 

# Hem bytes() fonksiyonu hem de encode() fonksiyonu aynı işlemi yapar. Bu fonksiyonlar yardımıyla str' den  bytes' lara çevrilen değerler decode() fonksiyonu ile bytes' lardan  str' lere tekrar dönüşür. 

#bytes fonksiyonuna 0-256 arasında sayılardan oluşan listeler de verilebilir.

# bytes fonksiyonu bir karakter dizisini bytes değer tipine dönüştürürken  fonksiyona dışarıdan verilen karakter kodlama tipiyle karakterleri çözer. Dönüştüreceği karakter dizisinde dışarıdan verilen  karakter kodlama tipinde uygun olmayan karakter varsa bu karakter yerine bazı karakterler koyar. Örneğin "?"

# bytes("ışık", encoding="ascii",errors="replace") # Output : b'???k' #ascii kodlamasında 'ı' ve 'ş' karakterlerinin bir karşılığı olmadığı için o karakterler yerine '?' koydu.

# bytes fonksiyonunun errors parametresinin aldığı değerler : replace, ignore, xmlcharrefreplace


# chr()  -> Verilen bir sayının karakter karşılığını döndürür. Bu fonksiyon karakterleri dönüştürürken ASCII karakter sistemini değil UNICODE karakter sistemini esas alır.

# list() -> Farklı veri tipindeki değerleri liste(list) tipine çevirmek için ve liste(list) tanımlamak için kullanılır.

# set() -> Farklı veri tipindeki değerleri set(küme) tipine çevirmek için ve set(küme) tanımlamak için kullanılır.

# tuple() -> Farklı veri tipindeki değerleri demet(tuple) tipine çevirmek için ve demet(tuple) tanımlamak için kullanılır.

# complex() -> Tam sayıları (int) ve kayan noktalı sayıları (float) karmaşık sayılara  (complex) dönüştürmek için kullanılır.

# int() -> Kayan noktalı sayıları ve eğer sayıya dönüşmeye uygunsa karakter dizilerini tam sayılara dönüştürür. Herhangi bir tabanda olan sayıyı onluk bir tabanda gösterebilmeyi sağlar.  

######### int("10",2) # 2 tabanındaki 10 sayısının 10'luk tabandaki değerini döndürür.

# float() -> Tam sayıları ve eğer uygun ise karakter dizilerini kayan noktalı sayıya dönüştürür.

# str() -> Tüm veri tiplerini karakter dizilerine dönüştürür.

# dict() -> Farklı veri tiplerinden sözlük(dict) tipinde veriler üretir.

######### dict(a=1,b=2,c=3)  # Output : {'a': 1, 'b': 2, 'c': 3}
######### dict(["a",1],["b",2],["c",3]) # Output : {'a': 1, 'b': 2, 'c': 3} 


# callable() -> Bir nesnenin ‘çagrılabilir’ olup olmadıgını denetler. Peki hangi nesneler çagrılabilir özelliktedir. Mesela fonksiyonlar çagrılabilir nesnelerdir. Degiskenler ise çagrılabilir nesneler degildir.

# ord() -> Karakterin UNICODE sisteminde karşılık geldiği sayıyı verir. chr() fonksiyonu ile ters mantıkta çalışır.



