# encoding: utf-8


class Solution:
    @staticmethod
    def linear_search():
        array_length_1 = int(input())
        array_1 = [int(x) for x in input().split()]
        array_length_2 = int(input())
        array_2 = [int(x) for x in input().split()]

        # print(len(set(array_1).intersection(set(array_2))))
        count = 0
        for i in range(array_length_2):
            if array_2[i] in array_1:
                count += 1
        print(count)


if __name__ == '__main__':
    solution = Solution()
    solution.linear_search()