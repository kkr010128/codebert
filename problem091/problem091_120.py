import sys
n = int(sys.stdin.readline().rstrip("\n"))
l = [int(s) for s in sys.stdin.readline().rstrip("\n").split()]
l.sort()
ans = 0
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            if l[a] != l[b] and l[b] != l[c] and l[a] != l[c]:
                if l[a] + l[b] > l[c]:
                    ans += 1
print(ans)