from bisect import bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def calc(m): #m以下の組が何通りあるかを数える
    count = 0 #組数を数える
    for a in A:
        b = m - a #b以上のは含める
        count += N - bisect_right(A, b - 0.5)
    return count

l = 0 
r = 3 * 10 ** 5

while r - l > 1:
    mid = (l + r) // 2
    if calc(mid) >= M: #合計mid以上の組と手を繋ぐとしたとき、とM回以上握手できる
        l = mid
    else:
        r = mid

B = [0] * (N + 1)
for i in range(N):
    B[i + 1] = B[i] + A[i]

# print(B)
flag = False
for i in range(mid + 3, -1, -1):
    if calc(i) < M:
        flag = False
    else: #初めて手をにぎる回数がM回を下回ったとき
        break

i += 1 #合計この値までは全て使う、残り回数を調整
ans = 0
for a in A:
    b = i - a
    tmp = bisect_right(A, b - 0.5)
    M -= (N - tmp) #使った数
    ans += a * (N - tmp) + (B[-1] - B[tmp])

ans += M * (i - 1)
print (ans)