import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = input().rstrip()

    if N % 2 == 1:
        ans = "No"
    else:
        if S[:N // 2] == S[N // 2:]:
            ans = "Yes"
        else:
            ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
