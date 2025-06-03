#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    @staticmethod
    def insertion_sort():
        # write your code here
        array_length = int(input())
        unsorted_array = [int(x) for x in input().split()]

        for i in range(array_length):
            v = unsorted_array[i]
            j = i - 1
            while j >= 0 and unsorted_array[j] > v:
                unsorted_array[j + 1] = unsorted_array[j]
                j -= 1
            unsorted_array[j + 1] = v
            print(" ".join(map(str, unsorted_array)))


if __name__ == '__main__':
    solution = Solution()
    solution.insertion_sort()