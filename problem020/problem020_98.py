from collections import deque


def print_list(que):
    for i, q in enumerate(que):
        if i != len(que)-1:
            print(q, end=' ')
        else:
            print(q)


def main():
    List = deque()
    n = int(input())
    for i in range(n):
        order = input().split()
        if order[0] == "insert":
            List.appendleft(order[1])
        elif order[0] == "delete":
            try:
                List.remove(order[1])
            except ValueError:
                pass
        elif order[0] == "deleteFirst":
            List.popleft()
        elif order[0] == "deleteLast":
            List.pop()
    print_list(List)


if __name__ == "__main__":
    main()

