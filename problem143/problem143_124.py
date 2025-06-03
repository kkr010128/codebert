K=int(input())
d=list(map(str,input().split()))
D=[]
for i in range(len(d[0])):
    D.append(d[0][i])
if len(D)<=K:
    print(''.join(D))
else:
    print(d[0][0:K]+'...')