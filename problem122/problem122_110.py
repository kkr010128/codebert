n = int(input())
a = list(map(int, input().split()))
q = int(input())

mp = {}
for i in a:
    mp[i] = mp.get(i, 0) + 1

total = sum(list(map(lambda item: item[0]*item[1], mp.items())))

for i in range(q):
    b, c = map(int, input().split())
    total -= b * mp.get(b, 0)
    total += c * mp.get(b, 0)
    mp[c] = mp.get(c, 0) + mp.get(b, 0)
    mp[b] = 0
    print(total)