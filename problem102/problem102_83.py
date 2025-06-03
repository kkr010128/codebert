import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,k = map(int,readline().split())
lst1 = list(map(int,readline().split()))

for i in range(n-k):
    if lst1[i] >= lst1[i+k]:
        print("No")
    else:
        print("Yes")