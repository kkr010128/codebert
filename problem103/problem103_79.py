N=input()
A=list(map(int,input().split()))

m=1000

tmp = A[0]
stock=0

for i,ai in enumerate(A):
    if tmp>=ai:
        m+=tmp*stock
        stock=0
        if ai < max(A[i:]):
            stock=m//ai
            m-=ai*stock
    tmp = ai
print(m+stock*A[-1])