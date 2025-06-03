n = int(input())
from copy import copy

L = ["a"]
if n == 1:
    print(L[0])
    exit()
    
for i in range(n-1):
    li = []
    for s in L:
        max1 = max(s)
        S = ""
        for j in range(ord(max1)-95):
            S = s + chr(97+j)
            #print(ord(max1)-95,chr(ord(max1)+j))
            li.append(S)
    L = copy(li)
    
print("\n".join(L))
