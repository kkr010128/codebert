n, k = map(int, input().split())
a = sorted(map(int, input().split()))
f = sorted(map(int, input().split()))[::-1]

# 成績　Σ{i=1~n}a[i]*f[i]
# a[i]小さいの、f[i]でかいの組み合わせるとよい(交換しても悪化しない)
def c(x):
    need = 0
    for i in range(n):
        if a[i] * f[i] > x:
            # f[i]を何回減らしてx以下にできるか
            diff = a[i] * f[i] - x
            need += 0 - - diff // f[i]
    return need <= k


l = 0
r = 1 << 60

while r != l:
    mid = (l + r) >> 1
    if c(mid):
        r = mid
    else:
        l = mid + 1
print(l)
