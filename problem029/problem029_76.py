r = list(map(float, input().split()))
print('{0:f}'.format(((r[2] - r[0]) ** 2 + (r[3] - r[1]) ** 2) ** 0.5))