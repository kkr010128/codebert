def main():
    n = int(input())
    for i in range(1, 11):
        if n > i * 1000:
            continue
        print(i * 1000 - n)
        return


if __name__ == '__main__':
    main()
