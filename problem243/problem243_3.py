def main():
    n = int(input())
    s_list = [None for _ in range(n)]
    t_list = [None for _ in range(n)]
    for i in range(n):
        s, t = input().split()
        s_list[i] = s
        t_list[i] = int(t)
    x = input()

    x_index = s_list.index(x)
    ans = sum(t_list[x_index + 1:])

    print(ans)


if __name__ == "__main__":
    main()
