def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    hand = ['r', 's', 'p']
    score = [p, r, s]
    dic_score = dict(zip(hand, score))
    win = [0] * n
    ans = 0
    for i in range(k):
        ans += dic_score[t[i]]
        win[i] = 1
    for i in range(k, n):
        if t[i] == t[i - k] and win[i - k]:
            continue
        ans += dic_score[t[i]]
        win[i] = 1
    print(ans)


if __name__ == '__main__':
    main()
