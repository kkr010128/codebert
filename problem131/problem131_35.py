import sys
input = sys.stdin.readline


def main():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())

    d = v - w

    if abs(a-b) <= t * d:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
