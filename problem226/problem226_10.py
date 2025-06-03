h,n = map(int,input().split())
A = list(map(int,input().split()))

if h-sum(A)>0 :
    print("No")
else:
    print("Yes")


