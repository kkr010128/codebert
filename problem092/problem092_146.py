if __name__ == "__main__":
    X, K, D = map(lambda x: abs(int(x)), input().split())

    if X - K*D >= 0:
        print(X - K*D)
    else:
        xdd = X // D
        k = xdd + (K - xdd) % 2
        print(abs(X - k*D))
