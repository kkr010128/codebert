from numba import njit


@njit
def main(X):
    for a in range(-200, 201):
        for b in range(-200, 201):
            if pow(a, 5) - pow(b, 5) == X:
                print(a, b)
                return


if __name__ == '__main__':
    X = int(input())
    main(X)
