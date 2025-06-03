from math import gcd
N = int(input())
A = list(map(int,input().split()))

g = A[0]
for i in range(1,N):
    g = gcd(g,A[i])

if g>1:
    print("not coprime")
    exit()

MAXN = 10**6 + 9
D = [i for i in range(MAXN+1)]
p = 2
while(p*p <=MAXN):
    if D[p]==p:
        for q in range(2*p,MAXN+1,p):
            if D[q]==q:
                D[q]=p
    p+=1

st = set()
for a in A:
    tmp = set()
    while(a>1):
        tmp.add(D[a])
        a //=D[a]
    for p in tmp:
        if p in st:
            print("setwise coprime")
            exit()
        st.add(p)

print("pairwise coprime")
