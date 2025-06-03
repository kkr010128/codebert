import sys
input = sys.stdin.readline

n = int(input())
a = [int(x) for x in input().split()]

max_a = [0]*(n + 1)
"""
if n == 0 and a[0] == 0:
    print(-1)
    sys.exit()
"""
for i in range(n + 1):
    if i == 0:
        max_a[i] = 1
    else:
        max_a[i] = (max_a[i - 1] - a[i - 1])*2
        if max_a[i] < 0:
            print(-1)
            sys.exit()
# print(max_a)
for i in range(n, -1, -1):
    if i == n:
        if max_a[i] < a[i]:
            print(-1)
            sys.exit()
        max_a[i] = a[i]
    else:
        min_p = max_a[i + 1] // 2 + int(max_a[i + 1] % 2 == 1)
        max_p = max_a[i + 1]
        if max_a[i] < min_p:
            print(-1)
            sys.exit()
        max_a[i] = min(max_p + a[i], max_a[i])
print(sum(max_a))
# print(max_a)


