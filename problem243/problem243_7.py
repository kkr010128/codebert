from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    N = ri()
    s = []
    t = []
    for i in range(N):
        x, y = input().split()
        s.append(x)
        t.append(int(y))
    X = rs()
    a = sum(t)
    b = 0
    for x, y in zip(s, t):
        b += y
        if x == X:
            break
    print(a - b)

if __name__ == '__main__':
    main()
