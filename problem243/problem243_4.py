def main():
    N = int(input())
    S = [0] * N
    T = [0] * N
    for i in range(N):
        S[i], T[i] = input().split()
    X = input()
    idx = S.index(X)
    ans = sum(map(int, T[idx+1:]))
    print(ans)


if __name__ == "__main__":
    main()
