from sys import stdin
rs = stdin.readline
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    N = ri()
    c = rs()
    x = 0
    y = c.count('R')

    for e in c:
        if x == y:
            break
        elif e == 'W':
            x += 1
        else:
            y -= 1

    print(y)

if __name__ == '__main__':
    main()
