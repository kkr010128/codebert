import math

N, X, T = map(int, input().split())

t = int(math.ceil(N/X))

print('{}'.format(t*T))
