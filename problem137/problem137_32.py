import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

if N % 2 == 1:
    i = N // 2
    AB.sort()
    L = AB[i][0]
    AB.sort(key=lambda x: x[1])
    R = AB[i][1]
    ans = R - L + 1
else:
    i = N // 2 - 1
    j = i + 1
    AB.sort()
    L = AB[i][0] + AB[j][0]
    AB.sort(key=lambda x: x[1])
    R = AB[i][1] + AB[j][1]
    ans = R - L + 1

print(ans)