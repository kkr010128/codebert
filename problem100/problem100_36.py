# coding: utf-8

# 識別する関数
def func(num):
    num = int(num)
    if 400 <= num and num <= 599:
        return 8
    elif 600 <= num and num <= 799:
        return 7
    elif 800 <= num and num <= 999:
        return 6
    elif 1000 <= num and num <= 1199:
        return 5
    elif 1200 <= num and num <= 1399:
        return 4
    elif 1400 <= num and num <= 1599:
        return 3
    elif 1600 <= num and num <= 1799:
        return 2
    else:
        return 1


if __name__ == "__main__":
    num = input()
    print(func(num))
