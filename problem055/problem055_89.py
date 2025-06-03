data = [None] * 4
for i in xrange(4):
    data[i] = [None] * 3
    for j in xrange(3):
        data[i][j] = [0] * 10

n = input()
for i in xrange(n):
    line = map(int, raw_input().split())
    data[line[0] - 1][line[1] - 1][line[2] - 1] += line[3]

for i in xrange(4):
    for j in xrange(3):
        s = ""
        for k in xrange(10):
            s += ' '
            s += str(data[i][j][k])
        print s
    if i < 3:
        print '#' * 20