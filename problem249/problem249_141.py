a, b, k = map(int, input().split())

t_fin = max(0, a - k)
a_fin = max(0, b - (k - (a - t_fin)))
print('{} {}'.format(t_fin, a_fin))
