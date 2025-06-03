x = int(input())
cnt = x // 100
y = x % 100
print(1 if cnt * 5 >= y else 0)