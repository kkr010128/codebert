#!/usr/bin/env python
# encoding: utf-8


class Solution:
    @staticmethod
    def selection_sort():
        # write your code here
        array_length = int(input())
        unsorted_array = [int(x) for x in input().split()]

        count = 0
        for i in range(array_length):
            min_j = i
            for j in range(i, array_length):
                if unsorted_array[j] < unsorted_array[min_j]:
                    min_j = j
            unsorted_array[i], unsorted_array[min_j] = unsorted_array[min_j], unsorted_array[i]
            if i != min_j:
                count += 1

        print(" ".join(map(str, unsorted_array)))
        print(str(count))


if __name__ == '__main__':
    solution = Solution()
    solution.selection_sort()