def main():
    n, m = map(int, input().split())
    h_lst = list(map(int, input().split()))

    ab_dict = dict()  # 展望台i : [展望台iに隣接する展望台の標高]
    for _ in range(m):
        a, b = map(int, input().split())

        if a not in ab_dict:
            ab_dict[a] = [h_lst[b - 1]]
        else:
            ab_dict[a].append(h_lst[b - 1])

        if b not in ab_dict:
            ab_dict[b] = [h_lst[a - 1]]
        else:
            ab_dict[b].append(h_lst[a - 1])

    cnt = 0
    ab_dict_keys = ab_dict.keys()
    for i in range(1, n + 1):
        if i not in ab_dict_keys:
            cnt += 1
            continue
        if h_lst[i - 1] > max(ab_dict[i]):
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
