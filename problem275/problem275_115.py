# A - DDCC Finals
def main():
    X, Y = map(int, input().split())
    prize_table = {1: 300000, 2: 200000, 3: 100000}
    prize = 0
    for rank in (X, Y):
        if rank in prize_table:
            prize += prize_table[rank]
    if X == Y and X == 1:
        prize += 400000
    print(prize)


if __name__ == "__main__":
    main()
