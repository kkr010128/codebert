from collections import Counter


def main():
    n = int(input())
    A = list(map(int, input().split()))
    a_c = Counter(A)
    a_s = list(set(A))
    tot = 0
    for a in a_s:
        tot += a_c[a] * (a_c[a] - 1) // 2
    ans = list(map(lambda x: tot - (a_c[x] - 1), a_s))
    ans_dic = dict(zip(a_s, ans))
    for a in A:
        print(ans_dic[a])


if __name__ == "__main__":
    main()