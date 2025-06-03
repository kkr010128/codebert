# coding:utf-8
# Doubly Linked List

from collections import deque

def main():

    n = int(input())
    dll = deque()

    for _ in range(n):
        operation = input().split(' ')
        if operation[0] in ["insert", "delete"]:
            key = operation[1]
            if operation[0] == "insert":
                dll.appendleft(key)
            else:
                try:
                    dll.remove(key)
                except:
                    pass

        else:
            if operation[0][6] == 'F':
                dll.popleft()

            else:
                dll.pop()

    print(' '.join(dll))

if __name__ == "__main__":
    main()