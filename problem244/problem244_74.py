def func(K, X):
    YEN = 500
    ans = 'Yes' if YEN * K >= X else 'No'
    return ans


if __name__ == "__main__":
    K, X = map(int, input().split())
    print(func(K, X))
