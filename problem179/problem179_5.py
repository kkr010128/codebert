N,M = list(map(int,input().split()))
a = list(map(int,input().split()))
a.sort(reverse=True)
if a[M-1]<sum(a)/(4*M):
    print("No")
else:
    print("Yes")
