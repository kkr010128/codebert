n = int(input())
a = list(map(int, input().split()))

result = 2020202020
num_left = 0
num_right = sum(a)

for i in range(n):
    num_left += a[i]
    num_right -= a[i]
    result = min(result, abs(num_left - num_right))
print(result)