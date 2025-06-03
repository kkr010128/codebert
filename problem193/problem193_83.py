import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    H, W, K = map(int, input().split())
    S = [tuple(map(int, list(input()))) for _ in range(H)]

    ans = 10 ** 9
    for bit in range(1 << (H-1)):
        canSolve = True
        order = [0] * (H + 1)
        tmp_ans = 0
        for i in range(H):
            if bit & 1 << i:
                order[i+1] = order[i] + 1
                tmp_ans += 1
            else:
                order[i+1] = order[i]
        sum_block = [0] * (H + 1)
        for w in range(W):
            one_block = [0] * (H + 1)
            overK = False
            for h in range(H):
                h_index = order[h]
                one_block[h_index] += S[h][w]
                sum_block[h_index] += S[h][w]
                if one_block[h_index] > K:
                    canSolve = False
                if sum_block[h_index] > K:
                    overK = True
            if not canSolve:
                break
            if overK:
                tmp_ans += 1
                sum_block = one_block
            if tmp_ans >= ans:
                canSolve = False
                break
        if canSolve:
            ans = tmp_ans
    print(ans)

if __name__ == '__main__':
    main()
