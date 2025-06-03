H,N=map(int,input().split())
lst=list(map(int,input().split()))
s=sum(lst)
if s>=H:
    print("Yes")
else:
    print("No")