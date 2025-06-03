import sys

n, k = map(int, input().split())
hn = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

ans = sum(hn[k:])
print(ans)