S, T = input().split(' ')
A, B = map(int, input().split(' '))
U = input()

d = {S: A, T: B}
d[U] -= 1

print('{} {}'.format(d[S], d[T]))
