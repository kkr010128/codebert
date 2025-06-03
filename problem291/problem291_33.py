import itertools
##print(ord("A"))
a,b,= map(int,input().split())
ans= a-b*2
if ans <=0:
    print(0)
else:
    print(ans)