def main():
    while True:
        cards = input();

        if cards == '-':
            break

        n = int(input())

        for _ in range(n):
            s = int(input())
            cards = (cards*2)[s:s+len(cards)]

        print(cards)

if __name__ == '__main__':
    main()

