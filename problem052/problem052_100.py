def call(n):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            res.append(str(i))
        elif '3' in str(i):
            res.append(str(i))
    print(' ' + ' '.join(res))

call(int(input()))