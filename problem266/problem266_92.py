# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    x = int(input().rstrip())

    if x // 100 * 5 >= x % 100:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    resolve()
