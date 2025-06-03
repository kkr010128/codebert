if __name__ == '__main__':
    N = int(input())
    l = input().split()
    num = [int(i) for i in l]

    print(min(num), max(num), sum(num))