import bisect
import sys
input = sys.stdin.readline

n,d,a= map(int, input().split())
x= [list(map(int, input().split())) for i in range(n)]

x.sort()
y=[]
for i in range(n):
    y.append(x[i][0])
    x[i][1]=-(-x[i][1]//a)

# どのモンスターまで倒したか管理しながら進める。
ans=0
# いつ効力が切れるか記録
z=[0]*(n+1)
# 今の攻撃力
atk=0
for i in range(n):
    atk+=z[i]
    if x[i][1]-atk>0:
        ans+=x[i][1]-atk
        q=bisect.bisect_right(y,x[i][0]+2*d,i,n)
        z[q]-=x[i][1]-atk
        atk+=x[i][1]-atk
print(ans)