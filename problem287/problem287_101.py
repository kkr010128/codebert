# -*- coding: utf-8 -*-

def main():

    N = int(input())

    case = []

    for i in range(1, 10):
        for j in range(1, 10):
            case.append(i * j)

    if N in case:
        ans = 'Yes'

    else:
        ans = 'No'

    print(ans)


if __name__ == "__main__":
    main()