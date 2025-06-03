n,m = map(int,input().split())

v1 = [ input().split() for _ in range(n) ]
v2 = [ int(input()) for _ in range(m) ]

l = [sum(map(lambda x,y:int(x)*y,v,v2)) for v in v1 ]

print(*l,sep="\n")