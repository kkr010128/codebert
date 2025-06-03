n = int(input())
a_int = list(map(int, input().split()))

height = 0
base = 0
for j in range(0, n - 1):
    if a_int[j] + base > a_int[j + 1] + base:
        base = a_int[j] - a_int[j + 1]
        height += base
        a_int[j + 1] += base
        base = 0
print(height)