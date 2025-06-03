n = int(input())
a = list(map(int, input().split()))
q = int(input())
total = sum(a)
dct = {}
for i in range(n):
    if a[i] in dct:
        dct[a[i]] += 1
    else:
        dct[a[i]] = 1

for i in range(q):
    b, c = map(int, input().split())
    if b not in dct: dct[b] = 0
    if c not in dct: dct[c] = 0
    total += dct[b] * (c - b)
    print(total)
    
    dct[c] += dct[b]
    dct[b] = 0