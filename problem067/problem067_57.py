def main():
    n = int(input())

    points = [0, 0]

    for i in range(n):
        t, h = input().split(' ')

        points = map(lambda x, y: x+y, points, judge(t, h))

    print("{0[0]} {0[1]}".format(list(points)))

def judge(t, h):
    if t < h:
        return (0, 3)
    elif t > h:
        return (3, 0)

    return (1, 1)

if __name__ == '__main__': main()