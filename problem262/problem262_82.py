n = int(input())
ans = [1]*n
T = [[-1]*n for _ in range(n)]
for ni in range(n):
    a = int(input())
    for ai in range(a):
        x, y = map(int,input().split())
        T[ni][x-1] = y

mx = 0
for i in range(pow(2,n)):
    tmx = -1
    B = bin(i)[2:].zfill(n)
    S = [i for i,b in enumerate(B) if b=='1']
    for s in S:
        _Ts = [i for i,t in enumerate(T[s]) if t==1]
        _Tf = [i for i,t in enumerate(T[s]) if t==0]
        if not (set(_Ts)<=set(S) and set(_Tf)&set(S)==set()):
            tmx = 0
            break
    if tmx==-1: tmx=len(S)
    mx = max(mx, tmx)
print(mx)