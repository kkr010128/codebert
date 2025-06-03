X,N=map(int,input().split())
p=list(map(int,input().split()))
i=0
j=0
while X+i in p:
    i+=1
while X-j in p:
    j+=1
if i>j:
    print(X-j)
elif i<j:
    print(X+i)
else:
    print(min([X+i,X-j]))
