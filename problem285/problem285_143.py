S=list(input())

s=0
f=0
g=0
h=0
for i in range(len(S)):
    if S[i]==">":
        g=0
        f+=1
        if h>=f:
            s+=f-1
        else:
            s+=f
        
    else:
        f=0
        g+=1
        s+=g
        h=g

print(s)
