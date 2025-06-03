from itertools import product
H, W, K = map(int, input().split())
choco = [list(input()) for _ in range(H)]

def cnt(array):
    count = [0] * H
    split_cnt = 0
    for w in range(W):
        for h in range(H):
            if choco[h][w] == "1":
                count[array[h]] += 1
        if any(i > K for i in count):
            split_cnt += 1
            count = [0] * H
            for h in range(H):
                if choco[h][w] == "1":
                    count[array[h]] += 1
            if any(i > K for i in count):
                return 10 ** 20
    return split_cnt

def get_array(array):
    l = len(array)
    ret = [0] * l
    for i in range(1, l):
        ret[i] = ret[i-1] + array[i]
    return ret

ans = 10 ** 20

for p in product(range(2), repeat=H-1):
    p = get_array([0]+list(p))
    ans = min(ans, cnt(p)+max(p))

print(ans)
