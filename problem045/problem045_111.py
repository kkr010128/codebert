(a, b) = [int(x) for x in input().split()]

di = a // b
m = a % b
df = a / b

print('{0} {1} {2:.8f}'.format(di, m, df))