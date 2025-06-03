import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    H, W, K = map(int, input().split())
    S = [tuple(map(int, list(input()))) for _ in range(H)]

    ans = 10 ** 9

    for bit in range(1 << (H-1)):
        canSolve = True
        ord = [0] * (H + 1)
        N = 0
        for i in range(H):
            if bit & 1 << i:
                ord[i+1] = ord[i] + 1
                N += 1
            else:
                ord[i+1] = ord[i]
        nums = [0] * (H + 1)
        for w in range(W):
            one = [0] * (H + 1)
            overK = False
            for h in range(H):
                one[ord[h]] += S[h][w]
                nums[ord[h]] += S[h][w]
                if one[ord[h]] > K:
                    canSolve = False
                if nums[ord[h]] > K:
                    overK = True
            if not canSolve:
                break
            if overK:
                N += 1
                nums = one
        if canSolve and ans > N:
            ans = N
    print(ans)

if __name__ == '__main__':
    main()
