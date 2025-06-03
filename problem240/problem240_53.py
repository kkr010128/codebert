def main():
    n, m = map(int, input().split())
    ac_list = [0 for _ in range(n + 1)] # 1: 正解済 0: 未正解
    wa_list = [0 for _ in range(n + 1)] 

    for _ in range(m):
        p, s = input().split()
        p = int(p)

        if ac_list[p] == 1: # 正解済
            continue
        
        if s == "AC":
            ac_list[p] = 1
        else:
            wa_list[p] += 1

    ac_count = 0
    wa_count = 0
    for i in range(1, n + 1):
        if ac_list[i] == 1:
            ac_count += 1
            wa_count += wa_list[i]

    print(ac_count, wa_count)


if __name__ == "__main__":
    main()
