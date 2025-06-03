# 解説
import sys
pin = sys.stdin.readline
pout = sys.stdout.write
perr = sys.stderr.write

N, M, K = map(int, pin().split())
A = list(map(int, pin().split()))
B = list(map(int, pin().split()))
a = [0]
b = [0]
for i in range(N):
    a.append(a[i] + A[i])
for i in range(M):
    b.append(b[i] + B[i])
ans = 0

for i in range(N + 1):
    #Aの合計がKを超えるまで比較する
    if a[i] > K:
        break
    # 超えていた場合に本の個数を減らす
    while b[M] > K - a[i]:
        M -= 1
    ans = max(ans, M + i)
print(ans)
