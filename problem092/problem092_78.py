def execute(X, K, D):
    for i in range(K):
        if X > 0:
            X -= D
        else:
            X += D

    return abs(X)

def execute2(X, K, D):
    T = int(abs(X) / D)
    if X > 0:
        if K < T:
            return X - K * D
        else:
            Y = X - T * D
            if (K - T) % 2 == 0:
                return Y
            else:
                return D - Y
    else:
        if K < T:
            return (X + K * D) * -1
        else:
            Y = X + T * D
            if (K - T) % 2 == 0:
                return -1 * Y
            else:
                return D + Y


if __name__ == '__main__':
    X, K, D = map(int, input().split())
    print(execute2(X, K, D))