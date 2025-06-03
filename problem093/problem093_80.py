def mod_max(loop, mod):
    if mod == 0:
        return 0
    loop_len = len(loop)
    mm = min(loop)
    for start in range(loop_len):
        current_sum = 0
        for i in range(mod):
            current_sum += loop[(start + i) % loop_len]
            mm = max(current_sum, mm)
    return mm


def main():
    n, k = map(int, input().split())
    p = [int(i) - 1 for i in input().split()]
    c = [int(i) for i in input().split()]

    seen = set()
    loop_list = []
    for start in range(n):
        v = start
        loop = []
        while v not in seen:
            seen.add(v)
            loop.append(c[v])
            v = p[v]
        seen.add(v)
        if loop:
            loop_list.append(loop)

    ans = min(c)
    for loop in loop_list:
        loop_len = len(loop)
        loop_num = k // loop_len
        loop_mod = k % loop_len
        loop_sum = sum(loop)
        ans = max(mod_max(loop, min(loop_len, k)), ans)
        if loop_num > 0:
            ans = max(loop_sum * loop_num + mod_max(loop, loop_mod), ans)
            ans = max(loop_sum * (loop_num - 1) + mod_max(loop, loop_len), ans)
    print(ans)


if __name__ == '__main__':
    main()
