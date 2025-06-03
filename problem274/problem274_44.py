N,M = map(int,input().split())
S = input()

c = 0
flag = 0
for i in S:
    if i == '0':
        if c >= M:
            flag = 1
            break
        c = 0
    else:
        c += 1
        
if flag == 1:
    print(-1)
else:
    T = S[::-1]
    now = 0
    ans = []
    while now != N:
        delta = 0
        for i in range(1,M+1):
            if now + i == N:
                delta = i
                break
            if T[now+i] == '0':
                delta = i
        ans.append(delta)
        now += delta
    Answer = ans[::-1]
    print(*Answer)