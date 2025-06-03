
h1,m1,h2,m2,k = map(int,input().split())

a = 60*(h2-h1)
b = m2-m1
##起きている合計時間
c = a+b
##勉強開始時間の最遅時間
d = c-k
print(d)