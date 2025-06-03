n = int(input())
a = list(map(int, input().split()))
first_half = 0
latter_half = sum(a)
min_diff = latter_half
for i in range(n):
    first_half += a[i]
    latter_half -= a[i]
    diff = abs(first_half - latter_half)
    min_diff = min(min_diff, diff)
print(min_diff)

