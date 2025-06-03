from copy import deepcopy

s = list(input())
k = int(input())

n = len(s)
if len(list(set(s))) == 1:
    print(n*k//2)
    exit()

n1 = 0
n2 = 0
s1 = deepcopy(s)
s2 = deepcopy(s) + deepcopy(s)

for i in range(n-1):
    if s1[i] == s1[i+1]:
        s1[i+1] = "?"
        n1 += 1

for i in range(2*n - 1):
    if s2[i] == s2[i+1]:
        s2[i+1] = "?"
        n2 += 1

d = n2 - n1

ans = n1 + d*(k-1)
print(ans)