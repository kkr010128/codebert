import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = list(map(int, input().split()))
h = list(map(int, input().split()))
ans = sum(item>=k for item in h)
print(ans)