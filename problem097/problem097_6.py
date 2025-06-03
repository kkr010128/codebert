K = int(input())

num = 0

for i in range(0,K):
    num = num*10 + 7
    if num % K == 0:
        print(i + 1)
        exit()

    num %= K

print(-1)
