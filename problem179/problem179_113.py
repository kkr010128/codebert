import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse = True)
sm = sum(a)
for i in range(M):
  if a[i] < sm / 4 / M:
    print("No")
    break
else: print("Yes")