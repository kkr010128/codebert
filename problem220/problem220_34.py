def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()

    print(A-1 if S == U else A, B if S == U else B-1)


if __name__ == "__main__":
    main()
