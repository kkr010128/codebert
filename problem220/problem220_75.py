def main():

    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        return " ".join(map(str, [A-1, B]))
    else:
        return " ".join(map(str, [A, B-1]))

if __name__ == '__main__':
    print(main())
