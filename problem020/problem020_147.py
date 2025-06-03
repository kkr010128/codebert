from collections import deque


def main():
    doubly_liked_list = deque()
    n = int(input())
    for i in range(n):
        command = input()
        if command == 'deleteFirst':
            doubly_liked_list.popleft()
        elif command == 'deleteLast':
            doubly_liked_list.pop()
        else:
            command = command.split()
            if command[0] == 'insert':
                doubly_liked_list.appendleft(int(command[1]))
            elif command[0] == 'delete':
                try:
                    doubly_liked_list.remove(int(command[1]))
                except:
                    pass
    print(*doubly_liked_list)


if __name__ == "__main__":
    main()

