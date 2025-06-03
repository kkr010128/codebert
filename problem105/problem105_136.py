# B - An Odd Problem
def main():
    _, *A = map(int, open(0).read().split())
    print(sum(i % 2 for i in A[::2]))


if __name__ == "__main__":
    main()
