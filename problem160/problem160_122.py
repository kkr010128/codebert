import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0


def resolve():
    def dfs(v, A):
        global res
        if len(A) == n:
            total = 0
            for a, b, c, d in query:
                if A[b - 1] - A[a - 1] == c:
                    total += d
            res = max(res, total)
        else:
            for i in range(v, m + 1):
                A.append(i)
                dfs(i, A)
                A.pop()

    n, m, q = map(int, input().split())
    query = [list(map(int, input().split())) for _ in range(q)]
    dfs(1, [])
    print(res)


if __name__ == '__main__':
    resolve()
