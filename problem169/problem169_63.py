N = int(input())
A = list(map(int,input().split()))
from collections import Counter
ctr = Counter(A)
ans = [ctr[i+1] for i in range(N)]
print(*ans, sep='\n')