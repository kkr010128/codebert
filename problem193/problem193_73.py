import itertools


def check(H, W, K, S, p):
    num_groups = p.count(True) + 1
    group_total = [0] * num_groups
    ret = p.count(True)

    for j in range(W):
        group_value = [0] * num_groups
        group_value[0] += int(S[0][j])
        group_idx = 0
        for i in range(H-1):
            if p[i]:
                group_idx += 1
            group_value[group_idx] += int(S[i+1][j])
        if max(group_value) > K:
            return float("inf")
        group_total_tmp = list(map(sum, zip(group_value, group_total)))
        if max(group_total_tmp) <= K:
            group_total = group_total_tmp
        else:
            group_total = group_value
            ret += 1
    return ret


def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = float("inf")
    for p in itertools.product([True, False], repeat=H-1):
        ans = min(ans, check(H, W, K, S, p))
    print(ans)


if __name__ == "__main__":
    main()
