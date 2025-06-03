#pythonじゃ通らなかった…(´・ω・`)
n = int(input())
a = list(map(int,input().split()))
ans = [[0 for i in range(n+1)] for j in range(n+1)]
p = []

#それぞれの活発度と元々居た位置の記録
for i in range(n):
    p.append([a[i],i])
p.sort(reverse=True)

#活発度の高い順にそれぞれ左と右から詰めて並べていく時のうれしさの変化
for i in range(1,n+1):
    ans[0][i] = ans[0][i-1] + p[i-1][0]*abs(p[i-1][1]-i+1)
for i in range(1,n+1):
    ans[i][0] = ans[i-1][0] + p[i-1][0]*abs(n-i-p[i-1][1])

#Douteki Planning 活発度の高い順に左にi人、右にj人詰めて並べていった時の最大値
for i in range(1,n):
    for j in range(1,n-i+1):
        ans[i][j] = max(ans[i][j-1] + p[i+j -1][0]*abs(p[i+j -1][1]-j+1),
        ans[i-1][j] + p[i+j - 1][0]*abs(n-i-p[i+j-1][1]))

#全て詰め並べ終わったときのうれしさの最大値(=答え)を探す
ma = 0
for i in range(n):
    ma = max(ma,ans[0+i][n-i])
print(ma)