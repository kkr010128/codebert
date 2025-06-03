
def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    a = X // D
    ans = 0
    if a <= K:
        K -= a
        ans = X - D * a
        if K % 2 != 0:
            ans = abs(ans - D)
    else:
        ans = X - D * K
    print(ans)



if __name__ == "__main__":
    main()