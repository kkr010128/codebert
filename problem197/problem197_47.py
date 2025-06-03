import sys

if __name__ == "__main__":
    a, b, c = [int(x) for x in input().split(" ")]
    if a + b >= c:
        print("No")
        sys.exit(0)
    if 4 * a * b < (c - a - b) ** 2:
        print("Yes")
    else:
        print("No")
