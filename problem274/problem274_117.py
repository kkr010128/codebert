N,M = map(int,input().split())
S = input()

ans = []
i = N
while i > 0:
    for m in range(M,0,-1):
        if i-m <= 0:
            ans.append(i)
            i = 0
            break
        if S[i-m]=='0':
            ans.append(m)
            i -= m
            break
    else:
        print(-1)
        exit()
print(*ans[::-1])
