k = int(input())
n = 7
for i in range(k):
    if n % k == 0:
        print(i+1)
        exit()
    n %= k
    n = (n*10+7) % k
print(-1)
