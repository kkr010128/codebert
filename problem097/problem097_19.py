K = int(input())
a = 7
flag = True

for i in range(K):
    if a % K == 0:
        print(i+1)
        flag = False
        break
    a = (a * 10 + 7) % K

if flag:
    print(-1)
