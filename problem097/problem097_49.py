k = int(input())
ans = 0
s = 7

for i in range(1, 10**6 + 1):
    s %= k
    if s == 0:
        print(i)
        exit()
    s = s*10 +7

print(-1) 