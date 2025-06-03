a, b = list(map(int, input().split()))
my_result = a * (a - 1) + b * (b - 1)
print(int(my_result / 2))