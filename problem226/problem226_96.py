h,n=map(int,input().split())
a=list(map(int,input().split()))

sum=0

for i in a:
    sum += i

if sum<h:
    print("No")
else:
    print("Yes")