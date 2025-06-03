from collections import deque

if __name__ == '__main__':
    n = int(input())
    dll = deque()
    for _ in range(n):
        command = input().split()
        if command[0] == 'insert':
            dll.appendleft(command[1])
        elif command[0] == 'delete':
            try:
                dll.remove(command[1])
            except ValueError:
                pass
        elif command[0] == 'deleteFirst':
            dll.popleft()
        elif command[0] == 'deleteLast':
            dll.pop()
    print(*dll)
