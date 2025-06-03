import itertools,sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
N = I()
A = LI()
ans = float('INF')
sum_A = sum(A)
accumulate_A = list(itertools.accumulate(A))
for i in range(N-1):
    ans = min(ans,abs(sum_A-accumulate_A[i]*2))
print(ans)
