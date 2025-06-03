n,m=map(int,input().split())
lst=list(map(int,input().split()))

if n<sum(lst) : print(-1)
else : print(n-sum(lst))