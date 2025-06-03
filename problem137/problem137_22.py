n = int(input())

a_line = []
b_line = []
for i in range(n):
    a, b = map(int, input().split())
    a_line.append(a)
    b_line.append(b)
    
a_line.sort()
b_line.sort()


if n % 2 == 0:
    left = a_line[n // 2 - 1] + a_line[n // 2]
    right = b_line[n // 2 - 1] + b_line[n // 2]
    print(right - left + 1)
else:
    print(b_line[n // 2] - a_line[n // 2] + 1)