# Python p112

##### 12. LİSTELER VE DEMETLERİN METOTLARI #####


liste=[i for i in range(10)]

liste.append(2) # 2 değerini listenin sonuna ekledi.

liste.extend([1,2,3,4]) # [1,2,3,4] listesini liste'ye ekledi. extend() metodu çoklu değer eklemek için kullanılır.

liste.insert(0,-1) # liste' nin 0. indeksine -1 değerini ekler.

liste.remove(-1) # liste içerisinde  geçen -1 değerini siler.

liste.pop(1) # liste içerisinde bulduğu ilk 1 değerini siler.

liste.sort() # liste'yi sıralar.

liste.index(2) # 2 değerinin ilk karşılaştığı yerdeki indeksini döndürür.

liste.count(2) # liste içerisinde geçen 2 elemanının sayısını döndürür.

# liste.clear() # liste' nin içeriğini temizler.

demet=(1,2,3,4,5,6,7,8,9)

demet.index(2) # 2 değerinin ilk karşılaştığı yerdeki indeksini döndürür.


