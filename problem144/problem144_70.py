import math


def abs(num):
    if num < 0:
        return -num
    return num


def main():
    abhm = [int(_x) for _x in input().split()]
    HL = abhm[0]
    ML = abhm[1]
    H = abhm[2]
    M = abhm[3]

    radian = 2.0 * math.pi * abs(M / 60.0 - (H + M / 60.0) / 12.0)

    length = math.sqrt(HL * HL + ML * ML - 2 * HL * ML * math.cos(radian))
    print(length)


main()
