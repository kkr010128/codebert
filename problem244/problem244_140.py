# -*- coding: utf-8 -*-

def main():

    K, X = map(int, input().split())

    money = 500 * K

    if money >= X:
        ans = 'Yes'

    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()