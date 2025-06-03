ans = ''
while True:
    m, f, r = map(int, input().split(' '))
    if (m == -1 and f == -1) and r == -1:
        break
    else:
        x = m + f
        if (m == -1) or (f == -1):
            ans += 'F\n'
        elif x >= 80:
            ans += 'A\n'
        elif x >= 65:
            ans += 'B\n'
        elif x >= 50:
            ans += 'C\n'
        elif x >= 30:
            if r >= 50:
                ans += 'C\n'
            else:
                ans += 'D\n'
        else:
            ans += 'F\n'
if ans != '':
    print(ans[:-1])
