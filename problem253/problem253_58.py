import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N, A, B = map(int, input().split())

dis = B - A
if dis % 2 == 0:
    ans = dis // 2
else:
    ans = min(A - 1, N - B) + 1 + ((B - A) // 2)

print(ans)
