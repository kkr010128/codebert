#queue
n,q=(int(i) for i in input().split())
nl=[]
t=[]
et=0
for i in range(n):
    na,ti=(j for j in input().split())
 #   print(t)
    nl.append(na)
    t.append(int(ti))
i=0
while len(nl)>0:
    t[i]-=q
    et+=q
 #   print(t)
    if t[i]<=0:
        et+=t[i]
        print(nl[i]+" "+str(et))
        nl.pop(i)
        t.pop(i)
        i-=1
    i+=1
    if i>=len(nl):
        i=0