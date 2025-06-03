import bisect

def main():
    N = int(input())
    S = input()
    R, G, B = [], [], []
    for i, s in enumerate(S):
        if s == 'R':
            R.append(i)
        elif s == 'G':
            G.append(i)
        else:
            B.append(i)

    global ans
    ans = 0
    count(R, G, B)
    count(R, B, G)
    count(G, R, B)
    count(G, B, R)
    count(B, R, G)
    count(B, G, R)
    print(ans)


def count(I, J, K):
    global ans
    for j in J:
        i_list = I[:bisect.bisect_left(I, j)]
        k_list = set(K[bisect.bisect_right(K, j):])
        remove = len([i for i in i_list if (2 * j - i) in k_list])
        ans += len(i_list) * len(k_list) - remove


if __name__ == '__main__':
    main()
