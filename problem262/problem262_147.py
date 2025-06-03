def main():
    n = int(input())
    xy = []
    for i in range(n):
        a = int(input())
        xy.append([tuple(map(int, input().split())) for _ in range(a)])

    c = 0
    for i in range(1 << n):
        popcnt = bin(i).count('1')
        if popcnt <= c:
            continue
        all_honest = True
        for j in range(n):
            if (1 << j) & i != 0:
                for x, y in xy[j]:
                    x -= 1  # 人の番号をひとつずらす
                    if ((1 << x) & i) >> x != y:
                        all_honest = False
                        break
            if not all_honest:
                break
        if all_honest:
            c = popcnt

    print(c)


if __name__ == '__main__':
    main()
