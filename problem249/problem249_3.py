a,b,k = map(int,input().split())
if a < k:
    print(max(0,a-k),max(0,b+a-k))
else:
    print(max(0,a-k),b)
