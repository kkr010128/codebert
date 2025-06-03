S, T = [s for s in input().split(' ')]
A, B = [int(s) for s in input().split(' ')]
U = input()
d = {S:A,T:B}

d[U] = d[U] - 1
print('%d %d' % (d[S], d[T]))
