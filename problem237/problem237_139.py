N = int(input())
K = []
for i in range(N):
    X,L = map(int,input().split())
    K.append([X-L,X+L])

T = sorted(K,key=lambda x:x[1])
a = T[0][1]

c = 1
for i in range(1,N):
    if T[i][0] >= a:
        c += 1
        a = T[i][1]
print(c)