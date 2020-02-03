# Python p111

##### 11. LİSTELER VE DEMETLER #####

liste=["object1","object2","object3"]

liste2=[i for i in range(0,10)]

#liste3=[if i%2==0 i  0 else for i in range(0,10)]

ifade="Python programlama dili."

ifade=list(ifade) # ifade değişkenini her harfi liste elemanı olacak şekilde yeniden tanımladı. Eğer list(ifade) değeri ifade değişkenine atanmaz ise ifadede herhangi bir değişim olmaz.


rliste=["karakter","ifade",1,2,3] # string ve integer tipi birarada liste tanımlanabilir.


sayilar=[]
for sayi in range(0,10):
    sayilar.append(sayi)

sayilar=sayilar[::-1] # sayilar listesini tersine çevirir.

sayilarparcasi=sayilar[3:6] # sayilar listesinden indeks değeri 3 olan elemandan indeks değeri 6 olan elemana kadar alır. 6.indeks hariç.


katmanli=[[1,2,3,4],"Ali","Veli","Ahmet",9,0,8] # Çok boyutlu liste.


katmanli[1]

aralik=range(12) # aralik listesinde range(0,12) listesini atar fakat aralik direk çağırma ile getirilemez.

print(*aralik)

liste=liste+[556] 

del liste[len(liste)-1] # liste adlı listenin son sıradaki elemanı silindi.

sartliListe=[i for i in range(50) if i%2==0]

##### Programı Bekletmek 

from time import sleep # Programa bir süre beklemesi için sleep modülünü eklendi.

sleep(2) # Program 2 saniye bekledi.

print("Günaydın")
