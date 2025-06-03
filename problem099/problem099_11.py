n, k = map(int, input().split())
a = list(map(int, input().split()))


def cut(x):
    cut_count = 0
    for i in range(n):
        cut_count += (a[i]-1)//x
    return cut_count


l = 0
r = 10**9
while r-l > 1:
    mid = (l+r)//2
    if k >= cut(mid):
        r = mid
    else:
        l = mid
print(r)

