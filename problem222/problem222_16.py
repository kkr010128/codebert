def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_set = set(a_list)

    if len(a_set) == n:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
