import sys
import itertools
import fractions
stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))

def frac2(p):
    return p//2

N,M=nm()
A=nl()
A=list(map(frac2,A))
min_bai=A[0]
for i in range(1,N):
    min_bai=min_bai*A[i]//fractions.gcd(min_bai,A[i])

for i in range(N):
    if((min_bai//A[i])%2==0):
        print(0)
        sys.exit(0)


tmp=M//min_bai
if(tmp%2==0):
    tmp-=1

print((tmp+1)//2)