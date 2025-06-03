def main(X, Y):
    for n_crane in range(X + 1):
        n_turtle = X - n_crane
        y = n_crane * 2 + n_turtle * 4
        if y == Y:
            print('Yes')
            return
    print('No')


if __name__ == "__main__":
    X, Y = [int(s) for s in input().split(' ')]
    main(X, Y)
