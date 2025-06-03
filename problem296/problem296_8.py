S=input()
K=int(input())
import copy
num=1
liS=[]

for i in range(len(S)-1):
    if S[i]==S[i+1]:
        num+=1
    else:
        liS.append(num)
        num=1
liS.append(num)



liSR=copy.copy(liS)
liSR[0]+=liSR[-1]
del liSR[-1]



if liSR!=[] and S[0]==S[-1]:
    for j in range(len(liS)):
        liS[j]=liS[j]//2
    for k in range(len(liSR)):
        liSR[k]=liSR[k]//2

    print(sum(liSR)*(K-1)+sum(liS))

elif liSR!=[] and S[0]!=S[-1]:
    for j in range(len(liS)):
        liS[j]=liS[j]//2
    print(sum(liS)*K)

else:
    print((sum(liS)*K)//2)

