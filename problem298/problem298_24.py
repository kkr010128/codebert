import bisect
n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

a = bisect.bisect(l, k-1)
print(n-a)