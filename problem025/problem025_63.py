if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    s = list(map(int, input().split()))

    def solve(i, mm):
        if mm == 0:
            return True
        if i >= n:
            return False
        if sum(t[i::]) < mm:
            return False
        res = solve(i + 1, mm) or solve(i + 1, mm - t[i])
        return res

    for r in s:
        print('yes' if solve(0, r) else 'no')

