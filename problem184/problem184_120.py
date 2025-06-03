import sys
input = sys.stdin.readline


def main():
    S = input().strip()
    assert len(S) == 6
    print("Yes") if S[2] == S[3] and S[4] == S[5] else print("No")


if __name__ == '__main__':
    main()
