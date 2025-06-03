n=int(input())
A=list(map(int,input().split()))

g=1000

for s1,s2 in zip(A[:-1],A[1:]):
    if s1<s2:
        stockNum=g//s1
        g+=stockNum*(s2-s1)

print(g)

