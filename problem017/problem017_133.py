#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def __init__(self):
        self.count = 0

    def shell_sort(self):
        array_length = int(input())
        array = []
        # array_length = 10
        # array = [15, 12, 8, 9, 3, 2, 7, 2, 11, 1]
        for m in range(array_length):
            array.append(int(input()))

        G = [1]
        while True:
            g = G[0] * 3 + 1
            if g > array_length:
                break
            G.insert(0, g)

        g_length = len(G)
        result = []
        for j in range(g_length):
            result = self.insertion_sort(array=array, array_length=array_length, g=G[j])
            # print(result, 'r', G[j])

        print(g_length)
        print(" ".join(map(str, G)))
        print(self.count)
        for k in range(array_length):
            print(result[k])

    def insertion_sort(self, array, array_length, g):
        # write your code here

        for i in range(g, array_length):
            v = array[i]
            j = i - g
            while j >= 0 and array[j] > v:
                array[j + g] = array[j]
                j -= g
                self.count += 1
            array[j + g] = v

        # print(" ".join(map(str, array)))
        return array


if __name__ == '__main__':
    solution = Solution()
    solution.shell_sort()