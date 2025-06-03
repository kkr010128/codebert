from collections import deque

if __name__ == "__main__":
    N = int(input())

    num_list = deque([])
    for i in range(N):
        command = input()
        if "insert" in command:
            key = command.split()[1]
            num_list.appendleft(key)
        else:
            if "First" in command:
                num_list.popleft()
            elif "Last" in command:
                num_list.pop()
            else:
                key = command.split()[1]
                if (key in num_list):
                    num_list.remove(key)

    print(" ".join(list(num_list)))

