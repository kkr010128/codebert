def main():
    number = int(input())
    queue = ["a"]
    for i in range(number - 1):
        now_queue = []
        for now in queue:
            limit = ord(max(now)) + 2
            for j in range(ord("a"), limit):
                now_queue.append(now + chr(j))
        queue = now_queue
    for q in queue:
        print(q)


if __name__ == '__main__':
    main()

