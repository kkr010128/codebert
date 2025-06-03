def print_it(l, n):
    print(''.join([l[x % 2] for x in range(n)]))

matrix = []
while True:
    values = input()
    if '0 0' == values:
        break
    matrix.append([int(x) for x in values.split()])

sc = ['#', '.']
cs = ['.', '#']
for height, width in matrix:
    for i in range(height):
        if 0 == i % 2:
            print_it(sc, width)
        else:
            print_it(cs, width)
    print()