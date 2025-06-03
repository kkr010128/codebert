import sys

n,k = map(int,input().split())
ans = 0;
h = [int(x) for x in input().split()]
h.sort(reverse = True)
h = h[k:]

if len(h) > 0:
    ans += sum(h)

print(ans)
