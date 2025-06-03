import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s,t = input().split()
a,b = map(int, input().split())
u = input()
if s==u:
    a -= 1
else:
    b -= 1
print(" ".join(map(str, (a,b))))