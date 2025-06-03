import sys 
from collections import Counter
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = list(map(int,readline().split()))
X = [0]*N
Y = [0]*N
for i in range(N):
    X[i] = (i+1) + A[i]
    Y[i] = (i+1) - A[i]  
cnt = Counter(Y)
ans = 0
for i in range(N):
    ans += cnt[X[i]] 
    cnt[Y[i]] -= 1
print(ans)