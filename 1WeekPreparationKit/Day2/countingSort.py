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


# -------------------------------HackerRank----------------

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'countingSort' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts INTEGER_ARRAY arr as parameter.
# #

# def countingSort(arr):
    
#     liste = [0]*100
    
#     for i in arr:
#         liste[i]+=1
        
#     return liste

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = countingSort(arr)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
