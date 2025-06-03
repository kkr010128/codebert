def main():
    N = int(input())
    A_ls = map(int, input().split(' '))
    ls = [0] * N
    for i in A_ls:
        ls[i - 1] += 1
    for i in ls:
        print(i)


if __name__ == '__main__':
    main()