X, Y= map(int,input().split())

a=2*X
b=(Y-a)/2
c=X-b

if(2*c+4*b==Y and (Y-a)%2==0 and c>=0 and b>=0):
    print("Yes")
else:
    print("No")
