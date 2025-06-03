# ABC172 Making Triangle
N = int(input())
L = list(map(int,input().split()))
d = {i:L.count(i) for i in L}

L = sorted(list(set(L)))
num = len(L)
ans = 0

for i in range(num-2):
    for j in range(i+1,num-1):
        for k in range(j+1,num):
            if L[k] < L[i] + L[j]:
                ans += d[L[k]]*d[L[i]]*d[L[j]]
            else:
                break
print(ans)