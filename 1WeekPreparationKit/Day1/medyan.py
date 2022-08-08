def medyanBul(vektor):
    vektor = sorted(vektor)
    veriAdedi = len(vektor)
    if veriAdedi % 2 == 1:
        print(vektor[veriAdedi // 2])
    else:
        i = veriAdedi // 2
        print((vektor[i - 1] + vektor[i]) / 2)
x= [1,2,3,4,5]
medyanBul(x)



# sorted() -> küçükten büyüğe sıralama (harf, sayı farketmez
# sum() -> liste içerisindeki sayıların toplamı

#!/bin/python3


#------------------------------------------------- HackerRank ----------------------
# import math
# import os
# import random
# import re
# import sys



# def findMedian(arr):
    
#     arr = sorted(arr)
#     lenght= len(arr)
    
#     if lenght%2==1:
#         return (arr[lenght//2])
#     else:
#         a=lenght//2 
#         return ((arr[a]+arr[a-1])/2)
        
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = findMedian(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
