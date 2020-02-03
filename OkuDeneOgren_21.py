# Python p121


###### 21. KÜMELER VE DONDURULMUŞ KÜMELER ######

# Kümeler Python üzerinde kullanılan, matematikte yer alan küme kavramıyla bağlantılı olan bir veri tipidir. 
# Matematikte kümeler üzerinde yapılan kesişim ve birleşim gibi özellikler Python Kümeler veri tipinde de geçerlidir.

# Kümeler de listeler ve sözlükler gibi değiştirilebilir bir veri tipidir.

# Kümeler de sözlükler gibi sırasız bir veri tipidir.

## Boş Küme

bos_kume=set() # set() fonksiyonu yardımıyla boş (hiç elemanı olmayan) bir küme oluşturuldu. Verinin tipi: set


# Küme tanımlamak

mskume=set(["Elma","Armut","Ayva","Muz"])


# Liste kullanarak küme tanımlamak

meyveKirmizi= ["Elma","Çilek","Nar","Vişne"]

mkkume=set(meyveKirmizi)


# Demet kullanarak küme tanımlamak

meyveTuruncu=["Portakal","Mandalina","Greyfurt"]

mtkume=set(meyveTuruncu)


# Karakter dizisi kullanarak küme tanımlamak

ifade="Python Programlama Dili"

kkume=set(ifade) # ifade içerisinde yer alan tüm karakterleri ayrı bir küme elemanı olacak şekilde tanımlar.  ifade değeri içerisinde bulunan karakter dizisi içerisindeki harfleri birer küme elemanı olarak tanımladık sonra bir harf  sadece bir defa yazılır. Yani kümeler bir elemanı birden fazla olarak tanımlansa bile kabul etmez, tek eleman olarak kaydeder. Kümeler bu özellikleriyle tıpkı matematikte yer alan kümeler gibi davranır.


# Sözlük veri tipi kullanarak küme tanımlamak

sozluk={"1":"Bir","2":"İki","3":"Üç"}

skume=set(sozluk) # sozluk adlı sözlük veri tipinin anahtar değerlerini kullanarak kümenin elemanlarını tanımlar.


# Sözlük veri tiplerinde bulunan anahtar,değer ikilileri bozulmadan da küme olarak tanımlanabilirler.

sliste=[(anahtar,deger) for anahtar,deger in sozluk.items()]

sskume=set(sliste)


# Kümeler tanımlanırken genelde (),[],{} parantez karakterleri kullanılmaz, ama yine de parantez ile küme tanımlanmak istenirse {} parantezleri ile tanımlanabilir..

susluKume={"Masa Lambası","Kalemlik","Defter","Kitap","Kalem","Silgi"}

type(susluKume) # susluKume olarak tanımlanan verinin tipinin "set" olduğu doğrulanabilir.

bosSusluKume={} # Boş süslü parantezler şekilde tanımlanan küme aslında küme değil sözlük tipinde bir veridir.

print(f"Boş süslü parantezlerle oluşturulan verinin tipi : {type(bosSusluKume)}") #f-string kullanılarak veri tipi ekrana yazdırıldı.



karakter="3333333333223333333332222233333333333223333332333333333"

karakterKumesi=set(karakter) # karakter değişkeni içerisinde sadece 2 ve 3 sayıları kullanıldığından karaterKumesi sadece 2 ve 3 elemanlarından oluşacaktır.


## Kümelerde Sıralanma Mekanizması

# Kümelerde bulunan elemanlarda indeks yapısı yoktur ve indeks kullanılarak çağırılamazlar. 

ornekListe=["Elma","Armut","Ayva","Muz","Limon"]

ornekKume=set(ornekListe) # Çıktı : {'Armut', 'Ayva', 'Elma', 'Limon', 'Muz'}

# print(ornekKume[2])

# Kümelerde elemanlar alfabetik sıraya göre(Türkçe karakterler ve büyük yazılan ifadeler sırayı bozar) sıralanır.


alfabe="qwertyuıopğüasdfghjklşizxcvbnmöç"

siraliKume=set(alfabe)


# Kümelerdeki en temel işlemlerden olan birleşme, keşisme ve fark işlemlerini gerçekleştirmek için en az iki kümenin olması gerekmektedir.
# Bu nedenle tek bir küme tanımlamak küme veri tiplerini etkin kullanmak açısından pek işlevsel değildir.


## Küme Üreteçleri ~ Set Comprehensions ##

import random

rliste=[random.randint(0,10000) for i in range(1000)] # 0-1000 arasında değişen 100 sayılık rastgele bir liste oluşturur.



Yuzden_Kucuk_Sayilar = [item for item in rliste if item<100]

#print(Yuzden_Kucuk_Sayilar) # Yuzden_Kucuk_Sayilar listesinde yüzden küçük bir sayı birden fazla yazılmış olabilir.

Yuzden_Kucuk_Sayilar_Kume={item for item in rliste if item<100}

print(Yuzden_Kucuk_Sayilar_Kume)


## Kümelerin Metotları


Kume_Metotlari=[]
for i in dir(set):
    if "__" not in i:
        Kume_Metotlari.append(i)
        
print(Kume_Metotlari)
        

kume_elemanlari=[1,2,3,4,5,6,7,23,56,"Elma","Armut","Limon","Ayva",34,456,0,-1]

ornkume=set(kume_elemanlari)


kopyaKume=ornkume.copy() # ornkume olarak tanımlanmış kümenin bir kopyası kopyaKume değişkenine atandı.

kopyaKume.clear() # kopyaKume kümesinin içeriği temizlendi.

# Kümeler sırasız veri tipleri olduklarından kopyaKume ile ornkume adlı kümelerin eleman dizilimi birbirlerinden farklıdır.

ornkume.add("Muz") # ornkume kümesine "Muz" elemanı eklendi.



# Bir kümeye herhangi bir öğe ekleyebilmemiz için, o öğenin değiştirilemeyen (immutable) bir veri tipi olması gerekiyor. 

# Bildiğiniz gibi Python’daki şu veri tipleri değiştirilemeyen veri tipleridir:

#  1.Demetler
#  2.Sayılar
#  3.Karakter Dizileri

# Şu veri tipleri ise değiştirilebilen veri tipleridir:

#  1.Listeler
#  2.Sözlükler
#  3.Kümeler

# Dolayısıyla bir kümeye ancak şu veri tiplerini ekleyebiliriz:

 # 1.Demetler
 # 2.Sayılar
 # 3.Karakter Dizileri


# İki Kümenin Farkı
 
k1=set([1,2,3,4,-1,-3,-5])
k2=set([3,4,5,2,4,24,9])
 
k1Farkk2=k1.difference(k2) # k1 de bulunan k2 de bulunmayan elemanlar.

k2Farkk1=k2-k1 # k2 de bulunan k1 de bulunmayan elemanlar.

ornkume.discard("Elma") # "Elma" adlı küme üyesini kümeden kaldırıldı.

ornkume.discard("dsffds") # Küme içerisinde yer almayan bir eleman silinmeye çalışılırsa program hata vermez.

ornkume.remove("sdgfdsa") # Küme içerisinde yer almayan bir eleman silinmeye çalışılırsa program hata verir.  

# discard() ve remove() metotlarının arasındaki en önemli fark hata mesajı verip vermemesidir.









