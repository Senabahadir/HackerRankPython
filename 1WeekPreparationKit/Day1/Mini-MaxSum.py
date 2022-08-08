arr = [1,2,3,4,5]

length = len(arr)
max_toplam =0
min_toplam =0
max_liste =[x for x in arr]
min_liste =[x for x in arr]

for i in range(length-1):
    a = max(max_liste)
    max_toplam +=a
    max_liste.remove(a)
        
for i in range(length-1):
    b = min(min_liste)
    min_toplam +=b
    min_liste.remove(b)
        
print(max_toplam, min_toplam)