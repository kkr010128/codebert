import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
i = 1
ans = 0
while i**2<=N:
    if N%i==0:
        ans = (i+(N//i)-2)
    i += 1
print(ans)