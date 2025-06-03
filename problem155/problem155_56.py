import sys
N,M=map(int,input().split())
H=list(map(int,input().split()))

#print(N,M,H)

bad=set()
for ln in sys.stdin:
    A,B=map(int,ln.split())
    x,y=H[A-1],H[B-1]
    if x>y:
        bad.add(B)
    elif x<y:
        bad.add(A)
    else:
        bad.add(A)
        bad.add(B)

print(N-len(bad))
