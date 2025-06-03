import sys
from collections import deque
input_lines = sys.stdin.readlines()

doublyLinkedList = deque()


for x in input_lines[1:]:
    oneLine = x.split()
    if 'insert' in oneLine[0]:
        doublyLinkedList.appendleft((int)(oneLine[1]))
    elif 'delete' == oneLine[0]:
        remove_value = (int)(oneLine[1])
        if remove_value in doublyLinkedList:
            doublyLinkedList.remove(remove_value)
    elif 'deleteFirst'in oneLine[0]:
        doublyLinkedList.popleft()
    elif 'deleteLast' in oneLine[0]:
        doublyLinkedList.pop()

print(*doublyLinkedList)