a,b,k=[int(i) for i in input().split()]
if(k>a):
    k=k-a
    a=0
elif(k<=a):
    a=a-k
    k=0
if(k>b):
    k=k-b
    b=0
elif(k<=b):
    b=b-k
    k=0
print(a,b)