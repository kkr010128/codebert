#!/usr/bin/env python3


def main():
    k = int(input())
    num = 0
    soeji = 0
    ar = [0 for _ in range(k)]

    while True:
        # print(soeji)
        if ar[soeji] > 0:
            break
        ar[soeji] = num
        soeji = (soeji * 10 + 7) % k
        num += 1

    print(-1 if ar[0] == 0 else ar[0])


if __name__ == '__main__':
    main()
