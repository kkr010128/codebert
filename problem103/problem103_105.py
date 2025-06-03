
N = int(input())
X = list(map(int, input().split()))

cur = 1000
stock = 0
state = 0  # 1=increase, 0=decrease
for i in range(N - 1):
    if state == 1 and X[i] > X[i + 1]:
        cur += X[i] * stock
        stock = 0
        state = 0
    elif state == 0 and X[i] < X[i + 1]:
        n = cur // X[i]
        cur -= X[i] * n
        stock += n
        state = 1

print(cur + stock * X[-1])
