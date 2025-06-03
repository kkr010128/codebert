from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
import queue
from collections import deque
from fractions import Fraction

# 10進数表記でnのk進数を求めてlength分0埋め
def ternary (n, k, length):
    if n == 0:
        nums = ['0' for i in range(length)]
        nums = ''.join(nums)
        return nums
    nums = ''
    while n:
        n, r = divmod(n, k)
        nums += str(r)
    nums = nums[::-1]
    nums = nums.zfill(length)
    return nums


def main():
    num = int(input())
    data = list(map(int, input().split()))
    mod = 10 ** 9 + 7

    max_length = len(bin(max(data))) - 2
    bit_count = [0 for i in range(max_length)]

    for i in range(num):
        now_bin = bin(data[i])[2:]
        now_bin = now_bin.zfill(max_length)
        for j in range(max_length):
            if now_bin[j] == "1":
                bit_count[j] += 1

    flg_data = [0 for i in range(max_length)]


    for i in range(max_length):
        flg_data[i] += bit_count[i] * (num - bit_count[i])

    ans = 0
    for j in range(max_length):
        pow_num = max_length - 1 - j
        bbb = pow(2, pow_num, mod)

        ans += bbb * flg_data[j]
        ans %= mod

    print(ans)




if __name__ == '__main__':
    main()

