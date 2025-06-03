import sys
input = sys.stdin.readline
import bisect
import collections
from collections import deque
n,d,a= map(int, input().split())
x= [list(map(int, input().split())) for i in range(n)]

x.sort()
y=[]
for i in range(n):
    y.append(x[i][0])
    x[i][1]=-(-x[i][1]//a)

# どのモンスターまで倒したか管理しながら進める。
# 累積ダメージを管理
qq=deque([])
ans=0
atk=0
for i in range(n):
    w=x[i][1]
    # iがダメージの有効期限を超過している場合
    while len(qq)>0 and i > qq[0][0]:
        atk-=qq[0][1]
        qq.popleft()

    if w-atk>0:
        ans+=w-atk
        q=bisect.bisect_right(y,x[i][0]+2*d)-1
        # 有効期限　ダメージ
        qq.append([q,w-atk])
        atk += w - atk
print(ans)