import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

def main():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 10 ** 9

    for bit in range(1 << (H-1)):
        canSolve = True
        ord = defaultdict(int)
        N = 0
        for i in range(H):
            if bit & 1 << i:
                ord[i+1] = ord[i] + 1
                N += 1
            else:
                ord[i+1] = ord[i]
        add = 0
        nums = defaultdict(int)
        for w in range(W):
            one = defaultdict(int)
            ok = True
            for h in range(H):
                one[ord[h]] += int(S[h][w])
                nums[ord[h]] += int(S[h][w])
                if one[ord[h]] > K:
                    canSolve = False
                if nums[ord[h]] > K:
                    ok = False
            if not ok:
                add += 1
                nums = one
        if canSolve and ans > N + add:
            ans = N + add
    print(ans)

if __name__ == '__main__':
    main()
