l,r,d= map(int,input().split())
print(sum([1 if t%d==0 else 0 for t in range(l,r+1)]))