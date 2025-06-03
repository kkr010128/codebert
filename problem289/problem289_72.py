import math
import sys
input = sys.stdin.readline


def main():
    a, b, x = map(int, input().split())
    x /= a
    h = x / a
    if h < b/2:
        t = 2 * x / b
        ans = math.degrees(math.atan(b/t))
    else:
        ans = math.degrees(math.atan(2*(b-h)/a))
    print(ans)


if __name__ == "__main__":
    main()
