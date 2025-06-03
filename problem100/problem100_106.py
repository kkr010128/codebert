def main():
    X = int(input())
    c = 600
    k = 8
    while True:
        if X < c:
            print(k)
            break
        c += 200
        k -= 1

if __name__ == '__main__':
    main()