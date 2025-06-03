dct = {
    0: (0, 0, 1),
    5: (0, 0, -1),
    2: (0, 1, 0),
    3: (0, -1, 0),
    1: (1, 0, 0),
    4: (-1, 0, 0)
}

def calc(x, y):
    res = (
        x[1] * y[2] - x[2] * y[1],
        x[2] * y[0] - x[0] * y[2],
        x[0] * y[1] - x[1] * y[0]
    )
    return res

if __name__ == "__main__":
    a = [int(x) for x in input().split()]
    Q = int(input())

    for _ in range(Q):
        x, y = map(int, input().split())
        
        for i, value in enumerate(a):
            if x == value:
                x_ind = i
            elif y == value:
                y_ind = i
        
        s, t = dct[x_ind], dct[y_ind]

        res = calc(s,t)
        for key in dct:
            if dct[key] == res:
                print(a[key])
                break

