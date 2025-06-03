from itertools import combinations_with_replacement

def main():
    N, M, Q = map(int, input().split())
    qs = [list(map(int,input().split())) for _ in range(Q)]
    seq = [i for i in range(1,M+1)]
    C = combinations_with_replacement(seq, N)
    max_score = 0

    for A in C:
        A = sorted(A)
        score = 0
        for q in qs:
            if A[q[1]-1] - A[q[0]-1] == q[2]:
                score += q[3]
        max_score = max(score, max_score)
    print(max_score)

if __name__ == '__main__':
    main()