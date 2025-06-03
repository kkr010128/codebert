dim = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d1 = [abs(x - y) for x, y in zip(a, b)]
print(sum(d1))

d2 = [(x - y)**2 for x, y in zip(a, b)]
print(pow(sum(d2), 1/2))

d3 = [(abs(x - y))**3 for x, y in zip(a, b)]
print(pow(sum(d3), 1/3))

print(max(d1))
