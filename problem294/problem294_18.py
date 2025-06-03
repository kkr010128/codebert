import sys, bisect

N = int(input())
L = list(map(int, sys.stdin.readline().rsplit()))
L.sort()

res = 0
for i in reversed(range(1, N)):
    for j in reversed(range(i)):
        l = bisect.bisect_left(L, L[i] + L[j])
        # r = bisect.bisect_right(L, abs(L[i] - L[j]))
        
        res += l - 1 - i
        
print(res)
