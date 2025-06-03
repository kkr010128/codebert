taro, hanako = 0, 0
n = int(input())
for _ in range(n):
    a, b = input().split()
    if a > b:
        taro += 3
    elif a < b:
        hanako += 3
    else:
        taro += 1
        hanako += 1
print(taro, hanako)