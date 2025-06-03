# A - Kth Term
def main():
    orig = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"
    seq = list(map(lambda s: s.strip(), orig.split(",")))
    K = int(input()) - 1
    print(seq[K])


if __name__ == "__main__":
    main()
