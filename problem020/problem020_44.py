from collections import deque


def main():
    d = deque()
    for _ in range(int(input())):
        command = input()
        if command[0] == 'i':
            d.appendleft(command[7:])
        elif command[6] == ' ':
            try:
                d.remove(command[7:])
            except ValueError:
                pass
        elif len(command) == 11:
            d.popleft()
        else:
            d.pop()
    print(*d)


if __name__ == '__main__':
    main()

