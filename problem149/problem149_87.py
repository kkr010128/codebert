from itertools import combinations

def is_achievable(M, X, A):
    result = [0] * M
    for a_row in A:
        for i, a in enumerate(a_row):
            result[i] += a

    for n in result:
        if n < X:
            return False
    return True

def main():
    N, M, X = map(int, input().split())

    C = [0] * N
    A = []

    for i in range(N):
        query = list(map(int, input().split()))
        C[i] = query[0]
        A.append(query[1:])

    if not is_achievable(M, X, A):
        print(-1)
        return
    
    index_C = [ i for i in range(N) ]
    min_cost = 10 ** 10
    for i in range(len(index_C)+1):
        for comb in combinations(index_C, i):
            cur_A = []
            cur_cost = 0
            for i in comb:
                cur_A.append(A[i])
                cur_cost += C[i]
            if is_achievable(M, X, cur_A):
                min_cost = min(min_cost, cur_cost)

    print(min_cost)

main()
