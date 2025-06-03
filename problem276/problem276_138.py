n = int(input())
a = list(map(int, input().split()))
hoge = [0] * n
cnt = 0
for i in range(n):
    #hoge[i + 1] = hoge[i] + a[i]
    cnt += a[i]
    hoge[i] = cnt
hoge_ = [0] * n
cnt = 0
for i in range(n - 1, -1, -1):
    cnt += a[i]
    hoge_[i] = cnt
ans = float('Inf')
for i in range(n - 1):
    ans = min(ans, abs(hoge[i] - hoge_[i + 1]))
print(ans)