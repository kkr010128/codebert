import sys


def solve(a_list):
    for a in a_list:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                return False
    return True


def main():
    input = sys.stdin.buffer.readline
    _ = int(input())
    a_list = list(map(int, input().split()))
    print("APPROVED" if solve(a_list) else "DENIED")


if __name__ == "__main__":
    main()
