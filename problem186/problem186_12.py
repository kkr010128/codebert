k, n = map(int,input().split())
a = list(map(int,input().split()))

n_1 = k - a[-1] + a[0]

l = [] # 各家間の距離リスト（i=1,2～）

for i in range(n-1):
    l.append(a[i+1]-a[i])
l.append(n_1)

print(k-max(l))