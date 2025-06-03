a, b = input().split()

A = a * int(b)
B = b * int(a)

lis = [A, B]

lis.sort()
print(lis[0])