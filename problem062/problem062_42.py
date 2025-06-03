import sys
def main():
    for x in sys.stdin:
        if x == "0\n":
            break
        else:
            X = list(x)
            total = 0
            for i in range(len(X) - 1):
                total += int(X[i])
            print(total)


if __name__ == "__main__":
    main()