def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline

    # 開催日数
    D = int(input())
    # 満足度の下がりやすさ
    C = list(map(int, input().split()))
    # 得られる満足度
    S = [ list(map(int, input().split())) for _ in range(D) ]
    # 開催予定
    T = [ int(input())-1 for _ in range(D) ]
    # 最後に開かれた日付
    last = [0]*26

    def cp(d, t):
        c = 0
        for i in range(26):
            c += C[i] * (d - last[i])
        return c

    score = 0
    for i in range(D):
        score += S[i][T[i]]
        last[T[i]] = i+1
        c = cp(i+1, T[i])
        score -= c
        print(score)


main()