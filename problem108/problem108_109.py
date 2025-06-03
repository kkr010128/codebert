def calc_change(price: int) -> int:
    return 1000 - price % 1000 if price % 1000 != 0 else 0


if __name__ == '__main__':
    print(calc_change(int(input())))
