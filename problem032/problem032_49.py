n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

diff = []
total1 = 0
total2 = 0
total3 = 0

for i in range(n):
    diff.append(abs(X[i] - Y[i]))
    total1 += diff[i]
    total2 += diff[i] ** 2
    total3 += diff[i] ** 3

print("{0:.6f}" . format(total1))
print("{0:.6f}" . format(total2 ** 0.5))
print("{0:.6f}" . format(total3 ** (1 / 3)))
print("{0:.6f}" . format(max(diff)))
