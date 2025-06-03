# AOJ ITP1_10_D

import math

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    n = int(input())
    x = intinput()
    y = intinput()
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    MD_INFTY = 0
    for i in range(n):
        MD_INFTY = max(MD_INFTY, abs(x[i] - y[i]))
        sum_1 += abs(x[i] - y[i])
        sum_2 += abs(x[i] - y[i]) ** 2
        sum_3 += abs(x[i] - y[i]) ** 3
    MD_1 = sum_1
    MD_2 = math.sqrt(sum_2)
    MD_3 = sum_3 ** (1 / 3)
    print(MD_1); print(MD_2); print(MD_3); print(float(MD_INFTY))

if __name__ == "__main__":
    main()
