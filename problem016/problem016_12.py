def bubbleSort(c):
    for i in range(len(c)):
        for j in range(len(c) - 1, i, -1):
            if c[j][1] < c[j - 1][1]:
                c[j], c[j - 1] = c[j - 1], c[j]
    return c


def selectionSort(c):
    for i in range(len(c)):
        minj = i
        for j in range(i, len(c)):
            if c[j][1] < c[minj][1]:
                minj = j
        c[i], c[minj] = c[minj], c[i]
    return c


n = int(input())
b = input().split()
s = b[:]

b = bubbleSort(b)
s = selectionSort(s)

print(*b)
print('Stable')
print(*s)
print('Stable' if b == s else 'Not stable')

