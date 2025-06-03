def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    num = 1
    for a in a_list:
        if a == num:
            num += 1
    
    if num == 1:
        print(-1)
    else:
        print(n - num + 1)


if __name__ == "__main__":
    main()
