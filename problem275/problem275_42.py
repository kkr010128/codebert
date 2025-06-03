# A - DDCC Finals
def main():
    X, Y = map(int, input().split())
    prize = 0
    for i in (X, Y):
        if i == 1:
            prize += 300000
        elif i == 2:
            prize += 200000
        elif i == 3:
            prize += 100000
    if X == Y and X == 1:
        prize += 400000
    print(prize)


if __name__ == "__main__":
    main()
