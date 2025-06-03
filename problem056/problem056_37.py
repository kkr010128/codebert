n,m = map(int,input().split())
#行列a、ベクトルb、行列積cの初期化
a = [0 for i in range(n)]
b = [0 for j in range(m)]
c = []
#a,bの読み込み
for i in range(n):
    a[i] = input().split()
    a[i] = [int(x) for x in a[i]]
for j in range(m):
    b[j] = int(input())
#行列積計算
temp = 0
for i in range(n):
    for j in range(m):
        temp += a[i][j]*b[j]
    c.append(temp)
    temp = 0
#結果の表示
for num in c:print(num)

