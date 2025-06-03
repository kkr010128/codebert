def main():
    A, B, C = map(int, input().split())
    K = int(input())

    while K > 0 and A >= B:
        B *= 2
        K -= 1

    while K > 0 and B >= C:
        C *= 2
        K -= 1

    if A < B < C:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()