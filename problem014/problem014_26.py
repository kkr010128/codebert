#!/usr/bin/env python
# encoding: utf-8


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    @staticmethod
    def bubble_sort():
        # write your code here
        array_length = int(input())
        unsorted_array = [int(x) for x in input().split()]

        flag = 1
        count = 0
        while flag:
            flag = 0
            for j in range(array_length - 1, 0, -1):
                if unsorted_array[j] < unsorted_array[j - 1]:
                    unsorted_array[j], unsorted_array[j - 1] = unsorted_array[j - 1], unsorted_array[j]
                    flag = 1
                    count += 1
        print(" ".join(map(str, unsorted_array)))
        print(str(count))


if __name__ == '__main__':
    solution = Solution()
    solution.bubble_sort()