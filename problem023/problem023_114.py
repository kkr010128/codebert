def main():
    n = int(input())

    s_set = set()
    for i in range(n):
        order = input().split()
        if order[0] == "insert":
            s_set.add(order[1])
        else:
            if order[1] in s_set:
                print("yes")
            else:
                print("no")


if __name__ == '__main__':
    main()

