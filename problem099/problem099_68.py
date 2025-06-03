n, k = map(int, input().split())
a = list(map(int, input().split()))

# binary search
left = 1
right = 10 ** 9

while left < right:
    center = (left + right) // 2

    total = 0
    for i in a:
        if i % center == 0:
            i -= 1
        total += i//center
    
    if total > k:
        left = center + 1
    else:
        right = center

print(left)