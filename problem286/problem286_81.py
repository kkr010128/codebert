import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b = list(map(int, input().split()))
if 1<=a<=9 and 1<=b<=9:
    ans = a*b
else:
    ans = -1
print(ans)