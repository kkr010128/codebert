n,m = map(int,input().split())

v1 = [ list(map(int,input().split())) for i in range(n) ]
v2 = [ int(input()) for i in range(m) ]

for v in v1:
    print( sum([ v[i] * v2[i] for i in range(m) ]))