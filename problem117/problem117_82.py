a,b,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

from itertools import accumulate

A = list(accumulate(A))
B = list(accumulate(B))
A = [0] + A
B = [0] + B

ans = 0
num = b
for i in range(a+1):
    if A[i] > k:
        continue
    while True :
        if A[i] + B[num] > k:
            num -=1
        else:
            ans = max(ans,i+num)
            break
print(ans)