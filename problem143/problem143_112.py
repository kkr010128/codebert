K=int(input())
S=input()
l=[]

if len(S)<=K:
    print(S)
else:
    for i in range(K):
        l.append(S[i])
    print("".join(l)+'...')