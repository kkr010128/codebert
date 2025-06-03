import numpy as np
N = int(input())
N_List = list(map(int,input().split()))
ans = (100**2)*100
for i in range(1,101):
    ca = sum(map(lambda x:(x-i)**2,N_List))
    if ca < ans:
        ans = ca

print(ans)
