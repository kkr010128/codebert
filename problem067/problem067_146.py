A, B = 0, 0
num = int(input())
for i in range(num):
    a, b = input().split()
    if a < b:
        B += 3
    elif a > b:
        A += 3
    else:
        A += 1
        B += 1
print(A, B)
