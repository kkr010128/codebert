import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b = map(int, input().split())
ab = str(a)*b
ba = str(b)*a
if ab<ba:
    ans = ab
else:
    ans = ba
print(ans)