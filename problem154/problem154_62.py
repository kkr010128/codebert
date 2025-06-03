n,k = map(int,input().split())
sunuke = []
for _ in range(k):
    d = input()
    tmp = [int(s) for s in input().split()]
    for i in range(len(tmp)):
        sunuke.append(tmp[i])

print(n - len(set(sunuke)))