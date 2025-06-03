n,m,l=map(int, input().split())
A=[ [ int(a) for a in input().split() ] for i in range(n) ]
B=[ [ int(b) for b in input().split() ] for i in range(m) ]
Bt=[ list(x) for x in zip(*B) ]
for a in A:
    print(" ".join(map(str, [ sum([ x*y for x,y in zip(a,b) ]) for b in Bt ])))