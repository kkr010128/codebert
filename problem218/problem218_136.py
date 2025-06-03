from collections import Counter


def main():
    n = int(input())
    S = [input() for _ in range(n)]
    S_c = Counter(S)
    num = list(S_c.values()).count(max(list(S_c.values())))
    anss = S_c.most_common()[:num]
    for ans in sorted(anss):
        print(ans[0])


if __name__ == '__main__':
    main()
