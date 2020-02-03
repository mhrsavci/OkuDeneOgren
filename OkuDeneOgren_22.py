# Python p122


###### 22. FONKSİYONLAR #####



## Fonksiyon 

# Fonksiyonların görevi, karmaşık işlemleri bir araya toplayarak, bu işlemleri  tek adımda yapılmasını sağlamaktır.Fonksiyonlar çoğu zaman, yapılmak istenen işlemler için bir şablon vazifesi görür. Fonksiyonları kullanarak, bir veya birkaç  adımdan oluşan işlemleri tek bir isim altında toplanabilir.Python’daki  ‘fonksiyon’ kavramı başka programlama dillerinde ‘rutin’ veya ‘prosedür’ olarak  adlandırılır.Gerçekten de fonksiyonlar rutin olarak tekrar edilen görevleri veya prosedürleri tek bir ad/çatı altında toplayan araçlardır.


def EkranaYazdir(): # def anahtar kelimesiyle fonksiyon ismiyle ve alabileceği parametreleri () ile gösterilerek tanımlanır.Buraı fonksiyonun başlığıdır.
    print("Merhaba, ben Fonksiyon!") # Fonksiyon çağrıldığı zaman hangi iş(ler)i yapacağı buraya yazılır. Burası fonksiyonun içidir.
    


EkranaYazdir() # Fonksiyon çağrılır.


## Uygulama Örneği 

# Birkaç bilgiyi tutmak için düzenlenmiş blokları fonksiyon ile oluşturmak 

def blokOlustur(blokHash,blokNum,trnNum,preBlokHash): # Fonksiyon parametrelere bağımlı olarak oluşturuldu.
    print("-"*30)
    print("Blok Şifrelenmiş Özeti: ",blokHash)
    print("Blok Numarası: ",blokNum)
    print("İşlem Sayısı: ",trnNum)
    print("Önceki Blok Şifrelenmiş Özeti: ",preBlokHash)
    print("-"*30)



## FONKSİYON ÖZELLİKLERİ
    

# 1. Python’da kabaca iki tip fonksiyon bulunur. Bunlardan biri gömülü fonksiyonlar (builtin functions), öteki ise özel fonksiyonlardır (custom functions). Burada ‘özel’ ifadesi, ‘kullanıcının ihtiyaçlarına göre kullanıcı tarafından özel olarak üretilmiş’ anlamına gelir.
    
# 2. Gömülü fonksiyonlar; Python geliştiricileri tarafından tanımlanıp dilin içine gömülmüş olan print(), open(), type(), str(), int() vb. fonksiyonlardır. Bu fonksiyonlar halihazırda tanımlanıp hizmetimize sunulduğu için bunları biz herhangi bir tanımlama işlemi yapmadan doğrudan kullanabiliriz.

# 3. Özel fonksiyonlar ise, gömülü fonksiyonların aksine, Python geliştiricileri tarafından değil, bizim tarafımızdan tanımlanmıştır. Bu fonksiyonlar dilin bir parçası olmadığından, bu fonksiyonları kullanabilmek için bunları öncelikle tanımlamamız gerekir.
    
    
# 4. Python’da bir fonksiyonun yaşam döngüsü iki aşamadan oluşur: Tanımlanma ve çağrılma.

# 5. Bir fonksiyonun çağrılabilmesi (yani kullanılabilmesi) için mutlaka birisi tarafından tanımlanmış olması gerekir.
    
# 6. Fonksiyonu tanımlayan kişi Python geliştiricileri olabileceği gibi, siz de olabilirsiniz. Ama neticede ortada bir fonksiyon varsa, bir yerlerde o fonksiyonun tanımı da vardır.
    
# 7. Fonksiyon tanımlamak için def adlı bir ifadeden yararlanılır. Bu ifadeden sonra, tanımlanacak fonksiyonun adını belirleyip iki nokta üst üste işareti konulur. İki nokta üst üste işaretinden sonra gelen satırlar girintili olarak yazılır. Daha önce de söylenildiği üzere bütün girintileme kuralları burada da geçerlidir.

# 8. Fonksiyonun adını belirleyip iki nokta üst üste koyduktan sonra, alt satırda girintili olarak yazdığımız bütün kodlar fonksiyonun gövdesini oluşturur. Doğal olarak, bir fonksiyonun gövdesindeki bütün kodlar o fonksiyona aittir. Girintinin dışına çıkıldığı anda fonksiyon tanımı da sona erer.
    
###############################################################################
    
## Öntanımlı Fonksiyon

def square(x=2): 
    print(x*x)

# Eğer square() fonksiyonu parametresiz çağırılırsa x=2 değerini dikkate alır ve fonksiyon 4 değerini döner.
# square() fonksiyonu parametreli olarak çağırılırsa (örneğin square(3) gibi) yazılan parametrenin karesini hesaplar.


## Sayısı belli olmayan isimsiz parametreli fonksiyon

def topla(*args): 
# topla() fonksiyonu içerisine yazılan ne kadar değer varsa toplar ve sonuc döndürür.
    sonuc=0
    for i in args:
        sonuc=sonuc+i
    print(sonuc)
# args parametresi ile verilen değerler birbirinden ayrık olmalıdır. Eğer bir dizi içerisinde birden fazla değer verilirse o dizi tek eleman kabul edilir ve öyle işlem yapılır.

## Sayısı belli olmayan isimli parametreli fonksiyon
    

def sozluk(**kwargs):
# sozluk() fonksiyonu aldığı birden fazla isimli parametreleri sözlük veri tipinde döndürür
    
    print(kwargs)

sozluk(isim="Ahmet",soyisim="Mehmet",meslek="Avukat",sehir="Aydın")
   
## **kwargs' lar anahtar kelimeleri yanlarında eşitlenen değere atayan sözlükler gibi davranır. Direkt olarak sözlükler de kwargs parametresi olarak kullanılabilir.



############################# Fonksiyon Örneği ################################

def karsilik_bul(*args, **kwargs):
    for sözcük in args:
        if sözcük in kwargs:
            print("{} = {}".format(sözcük, kwargs[sözcük]))
        else:
            print("{} kelimesi sözlükte yok!".format(sözcük))


sözlük = {"kitap"      : "book",
          "bilgisayar" : "computer",
          "programlama": "programming"}

karsilik_bul("kitap", "bilgisayar", "programlama", "fonksiyon", **sözlük)

###############################################################################


# return :  anahtar kelimesi fonksiyondan değer döndürür. Eğer tanımlanan bir fonksiyonda return ifadesi kullanılmazsa Python otomatik olarak None değeri döndürür.



def isimGetir():
    isim=input("İsim ne? ")
    print(isim)
    
#print(isimGetir()) # Burada çıktı olarak önce ilgili fonksiyonun çalıştırılması daha sonra da çıktı olarak fonksiyon çıktısı ile birlikte "None" değerinin dönmesi return anahtar sözcüğünü kullanmamaktan dolayıdır.


## random 


import random as rnd

liste=["1","Ahmet","Mehmet","3","5","234","5","2","90"]

rastgele=rnd.sample(liste,1) #liste adlı listeden rastgele 1 adet eleman seçti.

rnd.shuffle(liste) # listede yer alan elemanların yerlerini rastgele değiştirir.

rnd.randrange(0,100,10) # 0-100 arasında rastgele 10' nun katlarından sayı üretir.


## global Değişken Tanımlama


sayi=10

def degistir():
    global sayi # sayi global tipte tanımlanarak program sayfasının her yerinde 
#                 değiştirilebilir ve fonksiyon tekrar çağırıldığında da eski hali getirilir.
    sayi +=5
    print(sayi)
