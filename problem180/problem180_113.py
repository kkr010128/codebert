# アルゴリズムは回答を見て作成
n,k = map(int,input().split())
x = n
t = n%k
ans = min(t, k-t)
print(ans)