def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cum_A = [0]
    for a in A:
        if a + cum_A[-1] <= K:
            cum_A.append(a + cum_A[-1])
        else:
            break
    cum_B = [0]
    for b in B:
        if b + cum_B[-1] <= K:
            cum_B.append(b + cum_B[-1])
        else:
            break

    ans = 0
    max_b_idx = len(cum_B) - 1
    for a_idx, a in enumerate(cum_A):
        if a <= K and a_idx > ans:
            ans = a_idx
        for b_idx in reversed(range(max_b_idx + 1)):
            if a + cum_B[b_idx] <= K:
                max_b_idx = b_idx
                if a_idx + b_idx > ans:
                    ans = a_idx + b_idx
                break
    print(ans)


if __name__ == '__main__':
    main()
