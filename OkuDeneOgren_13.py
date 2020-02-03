# Python 113

##### 13. SAYMA SİSTEMLERİ #####

bin(456) # 456 sayısının ikili sayı sistemindeki karşılığını verir.

hex(456) # 456 sayısının onaltılı sayı sistemindeki karşılığını verir.

oct(456) # 456 sayısının sekizli sayı sistemindeki karşılığını verir.

int(456) # 456 sayısının onlu sayı sistemindeki karşılığını verir.

# Bilgisayarlar tüm işlemlerini ikili sayı sistemini kullanarak yapar.
# Bilgisayar terminolojisinde 0 ve 1 den oluşan herbir basamağa 'bit' adı verilir. Örneğin 15 sayısının ikili sayı sistemindeki karşılığı 1111 sayısı 4 bitlik bir sayıdır.

sayi=15

sayi.bit_length() # sayi değişkeninin ikili sistemde kaç basamak/bitten oluştuğunu döndürür.
