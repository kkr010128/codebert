# -*- coding: utf-8 -*-

def main():

    A = int(input())
    B = int(input())

    for i in range(1, 4):
        if i != A and i != B:
            ans = i

    print(ans)


if __name__ == "__main__":
    main()