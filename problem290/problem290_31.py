n,k = map(int,input().split())
a = list(map(int,input().split()))#消化コスト
f = list(map(int,input().split()))#食べにくさ
a.sort(reverse = True)
f.sort()
top = 10**13
bot = -1
def ok(x):
    res = 0
    for i in range(n):
        res += max(0,a[i] - (x//f[i]))
    return res <=k
while top - bot > 1:
    mid = (top + bot) //2
    if ok(mid):top = mid
    else:bot = mid
print(top)