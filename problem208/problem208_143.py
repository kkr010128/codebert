N,M = map(int,input().split())
S = []
C = []

for a in range(M):
    s,c = map(int,input().split())
    S.append(s)
    C.append(c)

a = ["0"]*N
e = []
for b,d in zip(S,C):
    if b in e:
        if str(d) != a[b-1]:
            print(-1)
            exit()
    elif b == 1 and d == 0:
        if N != 1:
            print(-1)
            exit()
    else:
        e.append(b)
        a[b-1] = str(d)

if a[0] == "0" and N != 1:
    a[0] = "1"
answer = ''.join(a)
answer = int(answer)
print(answer)