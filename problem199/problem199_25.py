import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    N = len(S)
    if N % 2 == 0:
        is_h = all(s == "h" for s in S[0::2])
        is_i = all(s == "i" for s in S[1::2])
        ans = "Yes" if is_h and is_i else "No"
    else:
        ans = "No"

    print(ans)


if __name__ == "__main__":
    main()
