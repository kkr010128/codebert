K = int(input())
tmp = 7
for i in range(1,K+1):
    if tmp%K == 0:
        print(i)
        exit()
    tmp = (tmp*10 + 7)%K
    tmp %= K
print(-1)