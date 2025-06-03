n,m=map(int,input().split())
k=m//2
for i in range (0,k):
    a=i+1
    b=2*k+1-i
    print (a,b)
c=2*k+2
k=(m+1)//2
j=1
#print(c,k)
for i in range (c,c+k):
    a=i
    b=c+2*k-j
    j+=1
    print(a,b)