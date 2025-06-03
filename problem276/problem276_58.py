from itertools import accumulate
n = int(input())
A = list(map(int,input().split()))
B = list(accumulate(A))
m = float("inf")
for i in B:
    m = min(m,abs(2*i-B[-1]))
print(m)