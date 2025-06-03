def minkowsuki(x, y, n):
    return sum(abs(x[i] - y[i]) ** n for i in range(len(x))) ** (1 / n)

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

print(minkowsuki(x, y, 1))
print(minkowsuki(x, y, 2))
print(minkowsuki(x, y, 3))
print(max(abs(x[i] - y[i]) for i in range(n)))