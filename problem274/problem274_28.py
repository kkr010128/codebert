N,M = map(int,input().split())
S = list(map(int,input()))

S.reverse()

#後ろから貪欲に

a = 0  #合計何マス進んだか
A = []  #何マスずつ進んでいるか

while a < N:
    if N-a <= M:
        A.append(N-a)
        a = N
    else:
        for i in range(M,0,-1):
            if S[a+i] == 0:
                A.append(i)
                a += i
                break
        else:
            print(-1)
            exit()

A.reverse()
print(*A)