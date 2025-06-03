n, k = map(int, input().split())
sunuke = []
for s in range(n):
    sunuke.append(str(s+1))

for t in range(k):
    d = int(input())
    hito = input().split(" ")
    for u in range(d):
        for v in range(n):
            if hito[u] == sunuke[v]:
                sunuke[v] = 0
            else:
                pass

m = sunuke.count(0)
print(n-m)