from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n
b = [0]*n

for i in range(n):
    a[i], b[i] = map(int, input().split())

a.sort()
b.sort()

if n%2!=0 :
    l = a[int(n/2)]
    u = b[int(n/2)]
    ans = u - l + 1
else:
    l = a[int(n/2-1)] + a[int(n/2)]
    u = b[int(n/2-1)] + b[int(n/2)]
    ans = u - l +1

print(ans)

