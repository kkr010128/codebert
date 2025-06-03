import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
c = 0
ans = -1
for num in a:
    if num==c+1:
        c = num
    else:
        pass
#     print(ans)
if c>0:
    ans = max(ans, c)
if ans>=0:
    print(n-ans)
else:
    print(-1)