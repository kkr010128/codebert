def main():
    x = int(input())

    for b in range(-200, 200):
        for a in range(b + 1, 200):
            if a ** 5 - b ** 5 == x:
                print(a, b)
                exit()


if __name__ == "__main__":
    main()
