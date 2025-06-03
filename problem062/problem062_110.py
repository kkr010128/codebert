#!usr/bin/env python3


def main():
    while True:
        numbers = input()
        if int(numbers) == 0:
            break
        res = 0
        for i in numbers:
            res += int(i)
        print(res)


if __name__ == '__main__':
    main()