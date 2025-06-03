import itertools
N=int(input())
S=input()

ans=0

for i in itertools.product(range(0,10),repeat=3):

    isOK=[False]*3
    
    for x in range(len(S)):
        if isOK[0] and isOK[1]:
            if int(S[x])==i[2]:
                ans+=1
                break
        elif isOK[0]:
            if int(S[x])==i[1]:
                isOK[1]=True
        else:
            if int(S[x])==i[0]:
                isOK[0]=True

print(ans)