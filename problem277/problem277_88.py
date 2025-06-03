H,W,K=map(int,input().split())
S=[input() for i in range(H)]
P=[[0 for i in range(W)] for m in range(H)]

for h in range(H):
    if "#" in S[h]:
        front=h
        break


m=0
x=0
for w in range(W):
    if S[front][w]=="#":
        m+=1
        for z in range(x,w+1):
            P[front][z]=m
        x=w+1
for z in range(x,W):
    P[front][z]=m

for h in range(front-1,-1,-1):
    for w in range(W):
        P[h][w]=P[h+1][w]


for h in range(front+1,H):
    if "#" in S[h]:
        x=0
        for w in range(W):
            if S[h][w]=="#":
                m+=1
                for z in range(x,w+1):
                    P[h][z]=m
                x=w+1
        for z in range(x,W):
            P[h][z]=m
    else:
        for w in range(W):
            P[h][w]=P[h-1][w]

for h in range(H):
    print(" ".join(list(map(str,P[h]))))
