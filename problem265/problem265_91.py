import math


def resolve():
    import sys
    input = sys.stdin.readline
    row1 = [int(x) for x in input().rstrip().split(" ")]
    s = row1[0]

    x = int(s / 1.08)

    if math.floor(x*1.08) == s:
        print(x)
    elif math.floor((x+1)*1.08) == s:
        print(x+1)
    else:
        print(":(")



if __name__ == "__main__":
    resolve()
