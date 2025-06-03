n,k = map(int,input().split())
A = list(map(int,input().split()))
imos = [0]*(n+1)
for j in range(k):
    if j==0:
        arr = A
    else:
        arr = imos
    imos = [0]*(n+1)
    for i,a in enumerate(arr):
        imos[max(i-a, 0)] += 1
        imos[min(i+a+1, n)] -= 1
    for k in range(1, len(imos)):
        imos[k] = imos[k]+imos[k-1]
    imos = imos[:-1]
    if set(imos)=={n}:
        break
print(*imos)