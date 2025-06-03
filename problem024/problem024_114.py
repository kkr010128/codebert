def ok(p,w,k):
    track= 1
    weight= 0
    flag= True
    for i in w:
        if i > p:
            flag=False
            break
        elif weight+ i> p:
            weight= i
            track+= 1
        else:
            weight+= i
    if track<=k and flag:
        return True
    else:
        return False
            

n,k= map(int, input().split())
w=[]
for i in range(n):
    w.append(int(input()))
    
l=0
h=10**11
while l+1 < h:
    p= (l+h)//2
    if ok(p,w,k):
        h= p
    else:
        l= p
print(h)
    
