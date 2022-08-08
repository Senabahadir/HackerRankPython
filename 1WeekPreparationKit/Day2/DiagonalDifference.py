arr = [[1,2,3],[4,5,6],[7,8,9]]

diagonal_top=0
horizontal_top=0

for i in range(0,len(arr)):
    diagonal_top+= arr[i][i]

for i in range(0, len(arr)):
    horizontal_top+= arr[i][len(arr)-1-i]

print(abs(horizontal_top-diagonal_top))


# ----------------HackerRank----------------

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'diagonalDifference' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts 2D_INTEGER_ARRAY arr as parameter.
# #

# def diagonalDifference(arr):
    
#     diagonal_top=0
#     horizontal_top=0

#     for i in range(0,len(arr)):
#         diagonal_top+= arr[i][i]

#     for i in range(0, len(arr)):
#         horizontal_top+= arr[i][len(arr)-1-i]

#     return abs(horizontal_top-diagonal_top)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()


# ---------------Numpy kütüphanesi ile çözüm aşağıdaki gibidir.-------------------

# import numpy as np

# arr = [[1,2,3],[4,5,6],[7,8,9]]
# for i in arr:
#     print(i)

# print(np.diag(arr))                  # diagonal
# print(np.fliplr(arr).diagonal())     # Horizontal flip

# # print(np.flipud(arr).diagonal())   # Vertical flip
# # print(np.diag(arr, k=1))           # k'ya 0,1,2 değerlerini vererek çıkan sonucu kontrol et.

# diagonal= np.diag(arr)
# horizontal= np.fliplr(arr).diagonal()

# top_diagonal=0
# top_horizontal=0

# for i in diagonal:
#     top_diagonal+=i
# for i in horizontal:
#     top_horizontal+=i

# print(abs(top_diagonal-top_horizontal))  # abs = mutlak değer
