import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())

    abm = [int(x) for x in input().rstrip().split(" ")]
    a_list = [int(x) for x in input().rstrip().split(" ")]
    b_list = [int(x) for x in input().rstrip().split(" ")]

    # 最小値
    ans = min(a_list) + min(b_list)

    for i in range(abm[2]):
        xyc = [int(x) for x in input().rstrip().split(" ")]
        price = a_list[xyc[0] - 1] + b_list[xyc[1] - 1] - xyc[2]
        if price < ans:
            ans = price

    print(ans)

if __name__ == "__main__":
    resolve()
