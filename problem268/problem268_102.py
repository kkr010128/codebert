if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    x, y, z = [0], [0], [0]
    for i in range(n):
        if a[i] == 0:
            if x[-1] == 0:
                x.append(1)
                y.append(y[-1])
                z.append(z[-1])
            elif y[-1] == 0:
                x.append(x[-1])
                y.append(1)
                z.append(z[-1])
            else:
                x.append(x[-1])
                y.append(y[-1])
                z.append(1)
        else:
            if x[-1] == a[i]:
                x.append(x[-1] + 1)
                y.append(y[-1])
                z.append(z[-1])
            elif y[-1] == a[i]:
                x.append(x[-1])
                y.append(y[-1] + 1)
                z.append(z[-1])
            else:
                x.append(x[-1])
                y.append(y[-1])
                z.append(z[-1] + 1)

    ans = 1
    for i in range(n):
        ans *= [x[i], y[i], z[i]].count(a[i])
        ans %= (10 ** 9 + 7)

    print(ans)
