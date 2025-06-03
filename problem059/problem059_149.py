ans = ''
r, c = map(int, input().split(' '))
i = 0
L = [0] * (c + 1)
while i < r:
    a = list(map(int, input().split(' ')))
    atot = 0
    j = 0
    while j < c:
        atot += a[j]
        L[j] += a[j]
        j += 1
    ans += ' '.join(map(str, a)) + ' ' + str(atot) + '\n'
    L[c] += atot
    i += 1
if ans != '':
    ans += ' '.join(map(str, L))
    print(ans)
