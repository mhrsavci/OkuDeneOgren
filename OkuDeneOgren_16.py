# Python p116


##### 16. DOSYALARIN METOT VE NİTELİKLERİ ######


# Dosyalar da tıpkı karakter dizileri veya listeler gibi bir veri tipidir.
# Dolayısıyla dosyalarında kendilerine has metotları vardır.

# Dosyaların Metotları:
d=open("deneme_21_11.txt","w")

for item in dir(d):
    if not item.startswith("_"):
        print(item,sep="\n")


# closed # Dosyanın kapalı olup olmadığını sorgular.

if not d.closed: # Eğer dosya kapalı değilse kapatır.
    d.close()

# readable() # Dosyanın okuma kipi ile açılıp açılmadığını sorgular.

# writable() # Dosyanın yazma kipi ile açılıp açılmadığının sorgular.

# truncate() # Dosyaların boyutlarını ayarlamak için kullanılır.


with open("deneme_21_11.txt","r+") as f:
    f.truncate() # Eğer truncate() metodu parametresiz olarak kullanılırsa dosyanın tüm içeriğini siler.

with open("deneme_21_11.txt","r+") as file:
    file.truncate(10) # Dosyanın 10 byte' lık kısmı hariç diğer kısımlarını siler. Dosyayı 10 byte olacak şekilde ayarlar.


# dosya=open("deneme_21_11.txt","r+")
# dosya.truncate(1024*10) # dosya adlı dosyayı 10 kb boyutuna yükseltir.
# dosya.close()

#with open("deneme_21_11.txt","r+") as dosya:
#    dosya.truncate(1024*10)


# mode # Dosyanın hangi rol (dosya kipi: w,r,x,a) ile açıldığını döndürür.

# name # Dosyanın hangi isim ile oluşturulduğunu döndürür.

# encoding # Dosyanın hangi dil kodlaması ile kodlandığını döndürür.


x=open("deneme_21_11_18.txt","w")

print(x.mode)

print(x.name)

x.close()








