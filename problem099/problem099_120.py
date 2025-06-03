N, K = map(int, input().split())
A = list(map(int, input().split()))

# 丸太がすべてxの長さ以下になる回数を出し、それがＫ回以下か判定する
def f(x):
    now = 0
    for i in range(N):
        now += (A[i]-1)//x
    return now <= K

l = 0
r = 10**9

while r-l > 1:
    mid = (r+l)//2
    if f(mid):
        r = mid
    else:
        l = mid
print(r)