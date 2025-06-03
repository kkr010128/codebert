from collections import deque


def main():
    s = input()
    q = int(input())
    d = deque(s)
    is_reversed = False

    for _ in range(q):
        query = list(input().split())

        if query[0] == "1":
            if is_reversed:
                is_reversed = False
            else:
                is_reversed = True

        elif query[0] == "2":
            if query[1] == "1":
                if is_reversed:
                    d.append(query[2])
                else:
                    d.appendleft(query[2])
            elif query[1] == "2":
                if is_reversed:
                    d.appendleft(query[2])
                else:
                    d.append(query[2])

    if is_reversed:
        print(*(list(d)[::-1]), sep="")
    else:
        print(*list(d), sep="")


if __name__ == "__main__":
    main()
