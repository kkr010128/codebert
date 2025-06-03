import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h, a = map(int, input().split())
ans = h//a + (h%a!=0)
print(ans)