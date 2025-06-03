import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())

ans = [0]*N
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            val = x**2+y**2+z**2+x*y+y*z+z*x
            if val<=N:
                ans[val-1] += 1

for v in ans:
    print(v)