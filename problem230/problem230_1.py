n,d,a = map(int,input().split())
xh = [list(map(int,input().split())) for _ in range(n)]

xh.sort()
j = 0
cnt = [0] * n
taken = 0

# def problem(h):
#     if h <= 0:return 0
#     ans = h//a
#     if h%a :
#         ans += 1
#     return ans

for i in range(n):
    [x,h] = xh[i]
    while xh[j][0] + 2*d < x:
        taken -= cnt[j]
        j += 1
    if taken * a >= h:
        continue
    if h % a == 0:
        cnt[i] = h//a - taken
    else:
        cnt[i] = h//a - taken + 1
    #cnt[i] = problem(h - taken * a)
    taken += cnt[i]
print(sum(cnt))
