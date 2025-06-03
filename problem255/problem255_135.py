N=int(input())
S,T=map(str,input().split())
l=[]
a,b=0,0
for i in range(N*2):
    if (i+1)%2!=0:
        l.append(S[a])
        a+=1
    else:
        l.append(T[b])
        b+=1
print(''.join(l))  