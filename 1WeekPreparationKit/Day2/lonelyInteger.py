liste = [1,1,2,2,3,3,4,5]

liste_tek = []
liste_tekrar =[]

for i in liste:
    if i not in liste_tek:
        liste_tek.append(i)

    else:
        liste_tekrar.append(i)


print(liste_tek)
print(liste_tekrar)
print("----------------")
for i in liste_tekrar:
    for j in liste_tek:
        if i ==j:
            liste_tek.remove(i)

print(liste_tek)
print(liste_tekrar)

for i in liste_tek:
    print(i)



# ---------------------------------------HackerRankKod---------

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'lonelyinteger' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY a as parameter.
# #

# def lonelyinteger(a):
    
#     liste_tek = []
#     liste_tekrar = []
    
#     for i in a:
#         if i not in liste_tek:
#             liste_tek.append(i)
            
#         else:
#             liste_tekrar.append(i)
            
#     for i in liste_tekrar:
#         for j in liste_tek:
#             if i ==j:
#                 liste_tek.remove(i)
    
    
#     for i in liste_tek:
#         return(i)
        

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     a = list(map(int, input().rstrip().split()))

#     result = lonelyinteger(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()
