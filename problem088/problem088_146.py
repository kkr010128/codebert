n = int(input())
aas = list(map(int, input().split()))
res = 0
pre = aas[0]
for i in range(1,len(aas)):
    if pre > aas[i]:
        res += pre - aas[i]
    else:
        pre = aas[i]
print(res)