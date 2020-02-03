# Python p104


#### 5. Kaçış Dizileri #####

#### 5.1. Ters Taksim (\)  #####

# Kaçış karakterleri yardımıyla tırnak içerisinde yazılamayacak, programın çalışırken karıştıracağı bazı özel karakterler yazılabilir.

print("\"Benim adım Sevgidir\" dedi") # Ters taksim yardımıyla çift tırnak içerisine çift tırnak kullanılarak bir ifade yazılabilir.

# Ters Taksim Nasıl Çalışır ?
#    Python bir karakter dizisini soldan sağa doğru okumaya başlar. Python karakter dizisini başlatan tırnak işaretini (örneğin tek tırnak) gördüğü zaman, soldan sağa doğru
#    ilerleyerek karakter dizisini bitirecek olan tırnağı (tek tırnağı) aramaya başlar.

print('\'Selam\' dedi dünyaya!')

#    Soldan sağa doğru ilerleyen Python tek tırnaktan önce gördüğü ters taksime bakarak aradığı tek tırnağın yani
#    karakter dizisini sonlandıran tek tırnağın bu olmadığını anlar ve karakter dizisini okumaya yardım eder.


# Ters Taksim yardımıyla çift tırnak içerisine yazılan uzun metinler alt satırlara bölünerek yazılabilir. (Tek tırnak için de böyle bir kullanım olabilir.)
print("Python, nesne yönelimli, yorumlamalı, birimsel ve \
etkileşimli yüksek seviyeli bir programlama dilidir.\
Girintilere dayalı basit sözdizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.\
Bu da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama \
yapılmaya başlanabilen bir dil olma özelliği kazandırır.")



#### 5.2. Satır Başı (\n)  #####


#Satır başı karakteri kendisinden sonra yazılan  ifadeleri bir alt satıra geçirir.
print("1. Mehmet\n2. Fatih\n3. Sultan\n4.Süleyman")

#Kaçış dizilerini iyi tanımak ekrana yazdırılan çıktılar açısından önemlidir. Örneğin:
#  C klasörü altında bulunan nisan dosyasının içerisinde masraflar.txt adlı bir text dosyası açılmak istendiğinde:
print("C:\nisan\masraflar.txt") # Burada \nisan kısmında \n ifadesi geçtiği için Python bunu satır başı karakteri ile karıştırır.
# Böyle bir durumda izlenebilecek iki yol vardır:

print("C:\\nisan\masraflar.txt")  # Ters taksim ile kaçış dizisinin özel bir karakter olduğu kaçış dizisi olmadığı Python a söylenir.

print(r"C:\nisan\masraflar.txt") # r ifadesi karakter dizisi içerisinde yazan kaçış dizilerini etkisizleştirir.

#### 5.2. Sekme (\t)  #####

print("Python\tDili") # Sekme kaçış dizisi kullanıldığı yerde sanki Tab tuşuna basmış gibi sonrasından gelen değeri öteler.


#### Etkisizleştirme (r)  #####

print(r"Kaçış Dizileri : \ , \n , \t, \N, \u") 
# Ekrana yazdırılmak istenen ifade kaçış dizileri içerdiği için doğru bir sonuç alınamayabilir. Fakat etkisizleştirme karakteri olan 'r' anahtar harfi başta kullanıldığında sorun çözülür.












