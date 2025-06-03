n=int(input())
s=input()
from itertools import product

cnt=0
for i,j in product("0123456789",repeat=2):
    try:
        ind_i=s.index(i)
    except:
        continue
    try:
        ind_j=s.rindex(j)
    except:
        continue
    if ind_i>ind_j:
        continue
    for k in "0123456789":
        cnt+=(k in s[ind_i+1:ind_j])
        
print(cnt)