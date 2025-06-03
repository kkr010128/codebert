n,k = map(int, input().split())
sunuke = []

for i in range(n):
    sunuke.append(1)

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        sunuke[a[j]-1] = 0

print(sum(sunuke))