# encoding: utf-8

import sys
from collections import deque


class Solution:
    @staticmethod
    def doubly_linked_list():
        # write your code here
        array_length = int(input())
        task_deque = deque()
        _input = sys.stdin.readlines()

        for i in range(array_length):
            l_arg = _input[i].split()
            action = l_arg[0]
            if len(l_arg) > 1:
                value = l_arg[-1]
            # print(action, 'v', value)

            if action == 'insert':
                task_deque.appendleft(value)
            elif action == 'deleteFirst':
                task_deque.popleft()
            elif action == 'deleteLast':
                task_deque.pop()
            elif action == 'delete':
                try:
                    task_deque.remove(value)
                except Exception as e:
                    pass
        print(" ".join(task_deque))


if __name__ == '__main__':
    solution = Solution()
    solution.doubly_linked_list()