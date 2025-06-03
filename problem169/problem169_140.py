import bisect
N = int(input())
A = [int(x) for x in input().split()]
A=sorted(A)
index = 0
for i in range(1, N+1):
    now = bisect.bisect_right(A, i)
    print(now - index)
    index = now
