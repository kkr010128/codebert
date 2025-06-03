i = list(map(int, input().split()))

a = i[0]
b = i[1]

print('{0} {1} {2:.5f}'.format(a // b, a % b, float(a / b)))