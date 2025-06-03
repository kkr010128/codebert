import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,K = MI()
A = LI()

from itertools import accumulate

for _ in range(min(K,41)):
    B = [0]*(N+1)
    for i in range(N):
        a = A[i]
        B[max(i-a,0)] += 1
        B[min(N,i+a+1)] -= 1
    C = list(accumulate(B))
    A = C

print(*[A[i] for i in range(N)])
