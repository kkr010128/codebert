a, b = list(map(int, input().split()))
remain = a - (b * 2)
print(remain if remain >= 0 else 0)