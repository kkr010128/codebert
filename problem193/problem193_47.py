import sys


def resolve(in_):
    H, W, K = map(int, next(in_).split())
    # n_choco = ord(b'0')
    w_choco = ord(b'1')
    S = [[1 if v == w_choco else 0 for v in line.strip()] for line in in_]
    # print(f'{H=} {W=} {K=}')
    # print(S)

    ans = 10000  # > (Hmax - 1) * (Wmax - 1)
    choco = [0] * H
    choco_temp = [0] * H
    for v in range(2 ** (H - 1)):
        # print(f'{v:04b}')
        ans_temp = sum(1 if v & (0b01 << i) else 0 for i in range(H - 1))
        for w in range(W):
            index = 0
            for h in range(H):
                choco_temp[index] += S[h][w]
                if v & (0b01 << h):
                    index += 1
            # print(f'b {choco=} {choco_temp=} {ans_temp=}')
            if all(a + b <= K for a, b in zip(choco, choco_temp[:index + 1])):
                # for i in range(len(choco)):
                for i in range(index + 1):
                    choco[i] += choco_temp[i]
                    choco_temp[i] = 0
            elif max(choco_temp) > K:
                ans_temp = 10000
                break
            else:
                # for i in range(len(choco)):
                for i in range(index + 1):
                    choco[i] = choco_temp[i]
                    choco_temp[i] = 0
                ans_temp += 1
            if ans_temp >= ans:
                break
            # print(f'a {choco=} {choco_temp=} {ans_temp=}')
        # print(f'{v:09b} {choco=} {ans_temp=}')
        ans = min(ans, ans_temp)
        for i in range(len(choco)):
            choco[i] = 0
            choco_temp[i] = 0
  
    return ans


def main():
    ans = resolve(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()
