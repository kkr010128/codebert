import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
d = list(map(int, input().split()))
ans = (sum(d)**2 - sum(item**2 for item in d))//2
print(ans)