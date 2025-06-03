from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

doubly_linked_list = deque()

for _ in range(n):
    command = input().split()
    if command[0] == "insert":
        doubly_linked_list.appendleft(command[1])
    elif command[0] == "delete":
        try:
            doubly_linked_list.remove(command[1])
        except:
            pass
    elif command[0] == "deleteFirst":
        doubly_linked_list.popleft()
    elif command[0] == "deleteLast":
        doubly_linked_list.pop()

print(" ".join(doubly_linked_list))
    

