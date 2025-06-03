m=str(raw_input())
n=[int(i) for i in m]
n.insert(0,0)
l=len(n)
ans=0
for i in range(l-1,-1,-1):
    current=n[i]
    if(current<5):
        ans+=current
    elif(current==5):
        ans+=current
        if(n[i-1]>=5):
            n[i-1]+=1
    else:
        ans+=10-current
        n[i-1]+=1
print ans
