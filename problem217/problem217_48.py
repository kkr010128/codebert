#!/usr/bin/env python3
def main():
    _ = int(input())
    A = [int(x) for x in input().split()]

    flag = True
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                pass
            else:
                flag = False
                break
    if flag:
        print('APPROVED')
    else:
        print('DENIED')


if __name__ == '__main__':
    main()
