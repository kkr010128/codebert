n = int(input())
a = n // 100
b = n % 100
check = a > 20 or b / 5 <= a
print("1" if check else "0")