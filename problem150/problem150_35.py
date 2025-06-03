def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    visited_list = [-1] * n  # 何ワープ目で訪れたか
    visited_list[0] = 0
    city, loop, non_loop = 1, 0, 0  # 今いる街、何ワープでループするか、最初にループするまでのワープ数

    for i in range(1, n + 1):
        city = a_list[city - 1]
        if visited_list[city - 1] != -1:
            loop = i - visited_list[city - 1]
            non_loop = visited_list[city - 1] - 1
            break
        else:
            visited_list[city - 1] = i

    city = 1
    if k <= non_loop:
        for _ in range(k):
            city = a_list[city - 1]
    else:
        for _ in range(non_loop + (k - non_loop) % loop + loop):
            city = a_list[city - 1]

    print(city)


if __name__ == "__main__":
    main()
