#!/usr/bin/env python3
def main():
    import time

    N = int(input())
    A = [int(x) for x in input().split()]

    num_lst = [0] * (N + 1)
    for a in A:
        num_lst[a] += 1

    ans = 0
    for num in num_lst:
        # ans += comb(num, 2, exact=True)
        ans += num * (num - 1) // 2

    start = time.time()
    for a in A:
        print(ans - (num_lst[a] - 1))
    end = time.time() - start
    # print(f'{end:6f}', 's')


if __name__ == '__main__':
    main()
