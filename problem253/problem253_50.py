import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,a,b = map(int, input().split())
if (b-a)%2==0:
    ans = (b-a)//2
else:
    m = b-1
    M = n-a
    m1 = (n-b) + 1 + (b-a-1)//2
    m2 = (a-1) + 1 + (b-a-1)//2
    ans = min(m,M, m1, m2)
print(ans)