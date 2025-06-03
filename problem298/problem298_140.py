from sys import stdin

n, k = [int(x) for x in stdin.readline().rstrip().split()]
h = [int(x) for x in stdin.readline().rstrip().split()]

ans = 0

for hi in h:
    if (hi >= k):
        ans += 1

print(ans)