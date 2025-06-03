def main():
    x, y = map(int, input().split())

    money = 0

    if x == 3:
        money += 100000
    elif x == 2:
        money += 200000
    elif x == 1:
        money += 300000

    if y == 3:
        money += 100000
    elif y == 2:
        money += 200000
    elif y == 1:
        money += 300000

    if x == 1 and y == 1:
        money += 400000

    print(money)


if __name__ == "__main__":
    main()
