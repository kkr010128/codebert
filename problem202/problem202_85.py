import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,A,B = MI()
q = N // (A+B)
r = N % (A+B)
print(q*A+min(r,A))
