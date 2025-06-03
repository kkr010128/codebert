def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    lst = [[i, x] for i, x in enumerate(a_list)]
    lst.sort(key = lambda x: x[1])

    for i in lst:
        print(i[0] + 1, end=" ")

if __name__ == "__main__":
    main()
