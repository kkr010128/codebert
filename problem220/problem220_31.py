dict = {}
S, T = input().split(' ')
dict[S], dict[T] = map(int, input().split(' '))
U = input()
dict[U] -= 1
print(dict[S], dict[T])