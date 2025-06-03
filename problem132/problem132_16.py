
from itertools import accumulate
def resolve():

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(K):
        imos_table = [0]*(N+1)
        for i, a in enumerate(A):
            # 配列の個数を超えないように注意
            imos_table[max(i - a, 0)] += 1
            imos_table[min(i + a + 1, N)] -= 1
        A = list(accumulate(imos_table))[:-1]
        if all([True if a == N else False for a in A]):
            print(*A)
            return
    else:
        print(*A)

if __name__ == "__main__":
    resolve()