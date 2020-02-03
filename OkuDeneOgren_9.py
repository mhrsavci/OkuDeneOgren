# Python p109


##### 9. KARAKTER DİZİLERİ EK KONULAR #####



kaynak = "şçöğüıŞÇÖĞÜİ" # Değişecek olan ifadeler.
hedef  = "scoguiSCOGUI" # Değişen ifadelerin yerine geçecek olan ifadeler.

çeviri_tablosu = str.maketrans(kaynak, hedef) # "Kaynak" ile "Hedef" ifadeleri eşleştirildi. "çeviri_tablosu" bir sözlük gibi davranır.

metin = "Bilindiği gibi, internet üzerinde bazı Türkçe karakterler kullanılamıyor."

print(metin.translate(çeviri_tablosu)) # "metin" karakter dizisi üzerinde bulunan "kaynak" değerler "hedef" değerler ile değiştirilir. translate() fonksiyonu "çeviri_tablosu" değişkenine göre "metin" üzerinde değişiklikler yapılır.

# isalpha() -> Karakter dizisinin alfabetik olup olmadığına bakar.

print(kaynak.isalpha()) # True

# isdigit() -> Karakter dizisinin sayısal olup olmadığına bakar.

deger="23456"
deger2="123456adf"

print(deger.isdigit()) # True

print(deger2.isdigit()) # False

# isalnum() -> Karakter dizisinin sayısal değerlerle alfabetik değerlerin birleşimi olup olmadığına bakar.

print(deger2.isalnum()) # True

deger3="1234sdf.,*-"

print(deger3.isalnum()) # False

# isidentifier() -> Bir karakterin değişken ismi olup olamayacağını kontrol eder.
# isdecimal() -> Bir karakter dizisinin noktalı noktasız sayı olmasına bakar.
# isspace() -> Bir karakter dizisinin sadece boşluklardan oluşup oluşmadığına bakar.


