
# coding: utf-8

# In[1]:

from math import sqrt

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i].uzaklik>alist[i+1].uzaklik:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

class Nokta:
    def __init__(self,x,y,sinif):
        self.x=x
        self.y=y
        self.sinif=sinif
class uzaklikBilgisi:
    def __init__(self,uzaklik,sinif):
        self.uzaklik=uzaklik
        self.sinif=sinif
def oklitMesafe(noktaListesi,newDot,k):
    mesafeListesi=[]
    for i in range(len(noktaListesi)):
        mesafe=uzaklikBilgisi(sqrt(((noktaListesi[i].x-newDot.x)**2)+((noktaListesi[i].y-newDot.y)**2)),noktaListesi[i])
        mesafeListesi.append(mesafe)
    bubbleSort(mesafeListesi) 
    
    sayac1=0
    sayac2=0
    for j in range(k):
        if mesafeListesi[j].sinif.sinif=="Sinif1":
            sayac1+=1
        elif mesafeListesi[j].sinif.sinif=="Sinif2":
            sayac2+=1
    if sayac1>sayac2:
        newDot.sinif="Sinif1"
    elif sayac2>sayac1:
        newDot.sinif="Sinif2"
    noktaListesi.append(newDot)    
    return noktaListesi

k=3
nk1=Nokta(7,7,"Sinif1")
nk2=Nokta(7,4,"Sinif1")
nk3=Nokta(3,4,"Sinif2")
nk4=Nokta(1,4,"Sinif2")
nk5=Nokta(3,7,"")
liste=[nk1,nk2,nk3,nk4]
d_deger=oklitMesafe(liste,nk5,k)
for i in range(len(d_deger)):
    print("x = ",d_deger[i].x,"y = ",d_deger[i].y,"Sinif = ",d_deger[i].sinif)
    
    


# In[ ]:




# In[ ]:



