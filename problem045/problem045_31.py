a, b = map(int, input().split())

print("{} {} {:.12f}".format(a // b, a % b, a * 1.0 / b))