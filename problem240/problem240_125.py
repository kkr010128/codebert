n,m = map(int, input().split()) 

pena=[0]*(n+1)
seitou=[0]*(n+1)

for i in range(m):
    p,s = map(str,input().split()) 
    p=int(p)
    if s=="WA" and seitou[p]==0:
        pena[p]+=1
    if s=="AC":
        seitou[p]=1

pena_kazu=0

for i in range(1,n+1):
    if seitou[i]==1:
        pena_kazu+=pena[i]

seitou_kazu=sum(seitou)

print(str(seitou_kazu)+" "+str(pena_kazu))