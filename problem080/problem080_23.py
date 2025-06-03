"""
四隅に仮想の原点をつくり、各座標からその原点へのマンハッタン距離を計測する。
"""

N = int(input())
XY = [list(map(int,input().split())) for _ in range(N)]

def measure(originX,originY):
    origin = [originX,originY]
    XY.sort(key=lambda x: abs(x[0]-origin[0])+abs(x[1]-origin[1]))
    return abs(XY[-1][0]-origin[0])+abs(XY[-1][1]-origin[1])-(abs(XY[0][0]-origin[0])+abs(XY[0][1]-origin[1]))

ans = 0
ans = max(ans,measure(1,1))
ans = max(ans,measure(1,10**9))
ans = max(ans,measure(10**9,1))
ans = max(ans,measure(10**9,10**9))
print(ans)