from itertools import permutations


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    A = [i for i in range(1, N+1)]
    As = list(permutations(A))
    for i in range(len(As)):
        a = As[i]
        for j in range(len(a)):
            if a[j] != P[j]:
                break
        else:
            p_rank = i
            break

    for i in range(len(As)):
        a = As[i]
        for j in range(len(a)):
            if a[j] != Q[j]:
                break
        else:
            q_rank = i
            break
    print(abs(p_rank-q_rank))


if __name__ == '__main__':
    main()