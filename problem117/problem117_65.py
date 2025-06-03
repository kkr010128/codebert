n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aa = [0]
for i in a:
    aa.append(aa[-1]+i)
bb = [0]
for i in b:
    bb.append(bb[-1]+i)
ans = 0
j = m
for i in range(n+1):
    if aa[i] > k:
        break
    while aa[i] + bb[j] > k and j > 0:
        j -= 1
    ans = max(ans, i+j)
print(ans)