import sys,collections
input = sys.stdin.readline

N=input().rstrip()
A=list(map(int,input().split()))
Ac = collections.Counter(A)
Q = int(input())
for i in range(Q):
    B,C = list(map(int,input().split()))
    nb = Ac[B]
    Ac[C] += Ac[B]
    Ac[B] = 0

    if i==0:
        ans = 0
        for key,val in Ac.items():
            ans += key*val
    else:
        ans +=nb*C - nb*B
    
    print(ans)
