import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
XY = [list(mapint()) for _ in range(N)]
XY.sort(key=lambda x:x[0]+x[1])
ans_1 = abs(XY[0][0]-XY[-1][0])+abs(XY[0][1]-XY[-1][1])
XY.sort(key=lambda x:x[0]-x[1])
ans_2 = abs(XY[0][0]-XY[-1][0])+abs(XY[0][1]-XY[-1][1])
print(max(ans_1, ans_2))