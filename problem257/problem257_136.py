n = int(input())
P = list(map(int,input().split()))

k=0
bc=0
c=0
i=0
while k < n :
    if P[k]!=i+1 :
        bc+=1
    else:
        i+=1
        c+=1
    k+=1

if c==0 :
    bc = -1

print(bc)


