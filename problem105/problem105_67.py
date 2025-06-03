n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(0,n):
    if i%2==0 and a[i]%2==1:
        b+=1
    else:
        b==b

print(b)