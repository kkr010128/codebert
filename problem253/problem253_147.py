# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n, a, b = [int(x) for x in input().rstrip().split(" ")]

    if a > n - b + 1:
        tmp = a
        a = n - b
        b = n - tmp
    else:
        a = a - 1
        b = b - 1

    if (b - a) % 2 == 0:
        print(abs(a - b) // 2)
    else:
        count = a + 1 + ((b - a - 1) // 2)
        print(count)



if __name__ == "__main__":
    resolve()
