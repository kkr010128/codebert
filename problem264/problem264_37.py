def main(M_1: int, D_1: int, M_2: int, D_2: int):
    print(M_2 - M_1)


if __name__ == "__main__":
    M_1, D_1 = map(int, input().split())
    M_2, D_2 = map(int, input().split())

    main(M_1, D_1, M_2, D_2)
