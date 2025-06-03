from collections import deque

def process_command(dll, commands):
    for cmd in commands:
        # print(cmd)
        if cmd.startswith('insert') or cmd.startswith('delete '):
            t = cmd.split(' ')
            cmd = t[0]
            num_str = t[1]
        if cmd == 'insert':
            dll.appendleft(int(num_str))
        elif cmd == 'delete':
            if int(num_str) in dll:
                temp = []
                result = dll.popleft()
                while result != int(num_str):
                    temp.append(result)
                    result = dll.popleft()
                temp = temp[::-1]
                dll.extendleft(temp)
        elif cmd == 'deleteFirst':
            dll.popleft()
        elif cmd == 'deleteLast':
            dll.pop()
        # print(dll)
        # print('=' * 64)


if __name__ == '__main__':
    # ??????????????\???
    commands = []
    num = int(input())
    for i in range(num):
        commands.append(input())

    # ??????
    dll = deque()
    process_command(dll, commands)

    # ???????????????
    # dll.reverse()
    print('{0}'.format(' '.join(map(str, dll))))