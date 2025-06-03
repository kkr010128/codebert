def main():

    X, Y, Z = map(int, input().split())
    return " ".join(map(str, [Z, X, Y]))

if __name__ == '__main__':
    print(main())
