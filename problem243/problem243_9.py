def main():
    n = int(input())
    S, T = [], []
    for _ in range(n):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    x = input()
    print(sum(T[S.index(x) + 1:]))

if __name__ == '__main__':
    main()
