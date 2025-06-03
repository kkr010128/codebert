# A - Number of Multiples
def main():
    L, R, D = map(int, input().split())
    print(R // D - (L - 1) // D)


if __name__ == "__main__":
    main()
