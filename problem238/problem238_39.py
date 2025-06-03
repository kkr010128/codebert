N,K,S=map(int,input().split())
P=[]
for i in range(N):
    if i<K:
        P.append(str(S))
    else:
        if S<10**9:
            P.append(str(S+1))
        else:
            P.append(str(1))

print(" ".join(P))