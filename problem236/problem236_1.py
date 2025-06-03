def main():
    H = int(input())
    W = int(input())
    N = int(input())

    print((N-1)//max(H,W) + 1)

if __name__ == '__main__':
    main()