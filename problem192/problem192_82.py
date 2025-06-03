from collections import Counter
n = int(input())
A = list(map(int,input().split()))
Acount = Counter(A)

total = 0
for key in Acount.keys():
    total += Acount[key] * (Acount[key] - 1) // 2

for i in range(n):
    tmp = total
    tmp -= Acount[A[i]]*(Acount[A[i]]-1) // 2
    tmp += (Acount[A[i]]-1)*(Acount[A[i]]-2) // 2
    print(tmp)