def main(k, s):
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + "...")


if __name__ == "__main__":
    k = int(input())
    s = input()
    main(k, s)
