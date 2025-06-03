n, m = map(int, input().split())

temp = list(['?'] * n)

# print(temp)
if (m == 0):
    if (n == 1):
        ans = 0
    else:
        ans = '1' + '0' * (n - 1)

else:
    for _ in range(m):
        s, c = map(int, input().split())
        if (s == 1 and c == 0 and n >= 2):
            print(-1)
            exit()
        else:
            pass

        if (temp[s-1] == '?'):
            temp[s - 1] = str(c)
        elif (temp[s - 1] == str(c)):
            pass
        else:
            print(-1)
            exit()

    if (temp[0] == '?'):
        temp[0] = '1'

    ans01 = ''.join(temp)
    ans = ans01.replace('?', '0')

print(ans)
