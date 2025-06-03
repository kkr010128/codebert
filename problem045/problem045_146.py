a, b = list(map(int, input().split()))

print("{0} {1} {2}".format(a//b, a%b, format(a / b, '.5f')))