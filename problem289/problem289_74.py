import math


def main():
    a, b, x = map(int, input().split())
    if (a*b)*a/2 >= x:
        y = 2*x/(a*b)
        ans = math.degrees(math.atan((b/y)))
    else:
        y = (2*(a**2*b - x))/(a**2)
        ans = math.degrees(math.atan(y/a))
    print(ans)


if __name__ == "__main__":
    main()
