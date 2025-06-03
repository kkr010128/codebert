h,n = (int(a) for a in input().split())
a = list(map(int,input().split()))
if sum(a) >= h :
    print("Yes")
else : print("No")