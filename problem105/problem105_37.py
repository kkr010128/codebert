n = int(input())
a = list(map(int,input().split()))
p = 0

for i in range(n)[::2]:
    if a[i] % 2 != 0:
        p += 1

print(p)