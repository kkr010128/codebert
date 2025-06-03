# B - Product Max
def main():
    A, B, C, D = map(int, input().split())
    res = max(A * C, A * D, B * C, B * D)
    print(res)


if __name__ == "__main__":
    main()
