n,k = map(int,input().split())
l = list(map(int,input().split()))

# xは求める長さ
def C(x):
    num = 0
    for i in range(n):
        # (a[i]-1)//x 回切る必要がある
        num += (l[i]-1)//x
    # k回以内に収まるか
    return num <= k

lb,ub = 0,max(l)
while ub-lb > 1:
    mid = (lb + ub) // 2
    # 条件を満たすならxを小さくしていく
    if C(mid):
        ub = mid
    else:
        lb = mid
    # print(lb,ub)

print(ub)