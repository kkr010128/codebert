def main():
    N = int(input())
    count = 0
    for a in range(N) :
        a += 1
        for b in range(N):
            b += 1
            c = N - a * b
            if c <= 0 :
                break
            else :
                count += 1

    print(count)

if __name__ == '__main__':
    main()
