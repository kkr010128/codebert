K = int(input())

n = 7
for i in range(1, 1000001):
    if n % K == 0:
        print(i)
        exit()
    n = (n * 10 + 7) % K
else:
    print(-1)