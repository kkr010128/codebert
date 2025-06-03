n = int(input())
point = [0, 0]
for i in range(n):
    a, b = input().split()
    if a > b:
        point[0] += 3
    elif a < b:
        point[1] += 3
    else:
        point[0] += 1
        point[1] += 1
print(*point)

