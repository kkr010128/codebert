import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
ans = 0
M = 10**9+7
for i in range(k, n+2):
    ans += (n-i+1+n)*(i)//2 - i*(i-1)//2 + 1
    ans %= M
#     print(i,ans)
print(ans%M)