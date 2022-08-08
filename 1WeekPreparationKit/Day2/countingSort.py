#100 sayılık bir liste içerisindeki sayılardan, tekrar eden sayıların 1 arttırıldığı kod. 
#Örneğin 5 sayısı 3 defa tekrar ettiyse count listesindeki 6.indexin değeri 3 olur.
import random
import numpy as np

arr = list(np.random.randint(low = 0,high=100,size=100)) #0 ve 100 aralığındaki random değerlerden oluşan 100 sayılık bir liste


print(arr)

count = [0]*100   #İçerisinde 100 tane 0 bulunan liste

for i in arr:
    count[i] +=1

print(count)