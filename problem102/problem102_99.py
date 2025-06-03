import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = MI()
A = [0] + LI()

for i in range(K+1,N+1):
    print('Yes' if A[i] > A[i-K] else 'No')
