# -*-coding:utf-8
#???????¨????

import math

def main():

    debtTime = int(input())

    ans = int(culcDebt(debtTime))

    print(ans)

def culcDebt(t):
    debt = 100000
    for i in range(t):
        debt = debt * 1.05
        debt = 1000 * math.ceil(debt/1000)

    return debt


if __name__ == '__main__':
    main()