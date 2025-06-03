S =  list(input())
K = int(input())
#print(S)
N=len(S)

#if K==1:
kosuu=[]
cnt=1
for i in range(N-1):
    if S[i]==S[i+1]:
        cnt+=1
        if i==N-2:
            kosuu.append(cnt)
    elif S[i]!=S[i+1]:
        kosuu.append(cnt)
        cnt=1
#print('kosuu', kosuu)
dammy=0
for i in range(len(kosuu)):
    dammy+=kosuu[i]//2

#else:
if K==1:
    out=dammy

elif S[0]!=S[-1]:
    out = dammy * K

elif len(S)==1:
    out=K//2

elif len(kosuu)==1:
    out=(kosuu[0]*K)//2

else:
    #kotei=kosuu[1:-1]  #少ないとき
    kotei = dammy - kosuu[0]//2 - kosuu[-1]//2
    aida = (kosuu[0] + kosuu[-1]) // 2
    #print('aida',aida)
    out = kosuu[0]//2 + (kotei*K) + aida*(K-1) + kosuu[-1]//2

print(out)