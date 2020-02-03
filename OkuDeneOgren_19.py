# Python p119

##### 19. BAYTLAR (BYTES) VE BAYT DİZİLERİ (BYTE ARRAYS) ######


# 2li sayma sisteminde her basamak 1 bit olarak adlandırılır.
# 8 adet bit birleşimiyle 1 bayt (byte) oluşur.
# 8 adet bit, yani toplam 1 bayt, Genişletilmiş ASCII sisteminde bir
#  adet karakteri temsil etmek için kullanılabilecek en büyük birim
#  olarak tasarlanmıştır.


# Python programlama dilinde karakter dizileri UNICODE kod konumları şeklinde temsil edilir. Dolayısıyla str adı verilen veri tipi esasında karakter dizilerini birtakım UNICODE kod konumları şeklinde gösteren soyut bir yapıdır. Yani biz Python’da karakter dizileri üzerinde işlem yaparken aslında baytlarla değil, UNICODE kod konumları ile muhatap oluyoruz. Ancak UNICODE kod konumları da tamamen soyut kavramlardır. Bunları bilgisayarın belleğinde bu şekilde temsil edemezsiniz ya da bu kod konumlarını herhangi bir ağ üzerinden başka bilgisayarlara iletemezsiniz. Bu kod konumlarını anlamlı bir şekilde kullanabilmek için öncelikle bunları bilgisayarların anlayabileceği bir biçim olan baytlara çevirmeniz gerekir. Çünkü dediğimiz gibi bilgisayarlar yalnızca bitler ve baytlardan anlar. İşte kod çözücülerin görevi de zaten bu kod konumlarını baytlara çevirmektir.


# Python2’de str veri tipi bize bir dizi bayt verir. Dolayısıyla bu veri tipinin içinde tuttuğu karakter dizisinin kaç bayt ile gösterileceği, sistemdeki öntanımlı kod çözücünün hangisi olduğuna bağlıdır. Kullandığınız işletim sisteminde öntanımlı kod çözücünün hangisi olduğunu şu komutla bulabilirsiniz:

import locale

print(locale.getpreferredencoding()) # Output: cp1254


# Eğer işletim sistemi Windows ise buradan alınacak çıktı muhtemelen cp1254 olacaktır. cp1254, Microsoft’un Türkçe için özel olarak kullandığı bir kod sayfası olduğu için, 128 ile 256 sayıları arasında Türkçe karakterleri içerir. O yüzden bu kodlama sisteminde Türkçe karakterler 1 bayt ile gösterilebilir. 


## İkili dosyalar okunurken elde edilen değerler karakter dizileri değil bayt olacaktır.
## İkili dosyalara ancak baytlar yazılabilir. Kısacası ikili dosya işlemlerinde bayt veri tipi kullanılır.

## Bayt veri tipi temel olarak ASCII karakterleri kabul eder. Dolayısıyla ASCII tablosu dışında kalan karakterleri doğrudan bayt olarak temsil edilemez.
## bytes() -> ASCII dışında kalan karakterleri bayt veri tipine dönüştürür.

b=bytes("ş","utf-8") # ş değerini utf-8 karakter kodlayıcısı ile kodlar(bayt tipine dönüştürür.)

d=bytes("ş","ascii",errors="xmlcharrefreplace") # Eğer ilgili değeri belirtilen karakter kodlayıcısını kullanarak kodlayamazsa error parametresinde ifade edilen kısım çalışır.


## encode() # Karakter dizilerinde ve bayt karakter dizilerinde de kullanılan encode metodu ile karakteri istenilen bir karakter kodlamasıyla kodlamak mümkündür.

i="İ".encode("utf-8") # Output: b'\xc4\xb0'

## decode() -> Karakter metotlarında olmayan fakat bayt karakter dizilerinde yer alan bir metotdur.encode() metodu kullanılarak yapılan kodlamayı geri çevirir.

# i=i.decode() # Output: "İ"
g=i.decode("cp1254") # Output: 'Ä°'

## bytes veri tipleri karakter dizileri gibi üzerlerinde değişiklik yapılamayan veri tipleridir. Değişiklik için veriyi başka bir değişkene kopyalamak,atamak gerekir.


























