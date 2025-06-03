n = int(input())
a, b = [[int(el) for el in input().split(' ')] for _ in range(2)]
print(sum(abs(a[i] - b[i]) for i in range(n)))
print(sum((a[i] - b[i]) ** 2 for i in range(n)) ** 0.5)
print(sum(abs(a[i] - b[i]) ** 3 for i in range(n)) ** (1/3))
print(max(abs(a[i] - b[i]) for i in range(n)))