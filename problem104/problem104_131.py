def main():
    L, R, d = map(int, input().split(' '))
    X = 0
    if L % d == 0:
        X = int(L / d) - 1
    else:
        X = int(L / d)
    print(int(R / d) - X)
main()