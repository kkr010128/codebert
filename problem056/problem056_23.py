n,m = map(int,input().split())

v1 = [ map(int,input().split()) for i in range(n) ]
v2 = [ int(input()) for i in range(m) ]

for v in v1:
    print(sum(map(lambda x,y:x*y,v,v2)))