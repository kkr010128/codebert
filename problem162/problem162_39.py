#ABC165-E Rotation Matching
"""
各頂点を円形に並べた時に、距離が等しくならないようにm個の辺を張れば良い。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m = map(int,readline().split())
mod = n
lst1 = []
for i in range(m):
    lst1.append(i)

lst2 = []
for i in range(m):
    lst2.append(2*m-1-lst1[i])

for i in range(m//2):
    lst2[i] -= 2*m+1

for i,j in zip(lst1,lst2):
    print(i%mod+1,j%mod+1)
