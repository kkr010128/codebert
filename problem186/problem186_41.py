k, n = map(int, input().split())
a = list(map(int, input().split()))

max_kyori = 0
a.append(k + a[0])

for i in range(1, n+1):
    kyori = a[i] - a[i-1]
    if(kyori > max_kyori):
        max_kyori = kyori

print(k - max_kyori)
