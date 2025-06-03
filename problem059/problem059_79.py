r, c = map(int, input().split())

sumOfCols = [0] * c

for i in range(r):
    cols = list(map(int, input().split()))
    s = sum(cols)
    sumOfCols = [p + q for p,q in zip(sumOfCols, cols)]
    print(' '.join(map(str, cols)), end=' ')
    print(s)


s = sum(sumOfCols)
print(' '.join(map(str, sumOfCols)), end=' ')
print(s)