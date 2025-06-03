def main():
    x, k, d = map(int, input().split())
    y = abs(x) // d
    if y == k:
        print(abs(x) % d)
    elif y < k:
        if (k-y) % 2 == 0:
            print(abs(x) % d)
        else:
            print(min(abs(abs(x) % d - d), abs(abs(x) % d + d)))
    else:
        print(min(abs(abs(x)-d*k), abs(abs(x)+d*k)))




if __name__ == '__main__':
    main()
