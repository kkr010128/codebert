# -*- coding: utf-8 -*-

def main():

    A, B = map(int, input().split())

    ans = A - 2 * B
    
    if ans < 0:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()