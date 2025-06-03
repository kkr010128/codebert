from math import sqrt

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
p_1 = 0
p_2 = 0
p_3 = 0
p_inf = 0
for i, j in zip(x, y):
    p_1 += abs(i - j)
    p_2 += (i - j) ** 2
    p_3 += abs((i - j)) ** 3
    p_inf = max(p_inf, abs(i - j))

print(p_1)
print(sqrt(p_2))
print(p_3 ** (1 / 3))
print(p_inf)
