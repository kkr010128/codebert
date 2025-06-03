import collections
n = int(input())
L = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if L[i]+L[j] > L[k] and L[k]+L[j] > L[i] and L[i]+L[k] > L[j]:
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    ans += 1
print(ans)