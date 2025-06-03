
def sum_dict(d):
    num = 0
    for k, v in d.items():
        num += k * v
    return num


def create_dict(A):
    d = {}
    for a in A:
        if d.get(a) is None:
            d[a] = 1
        else:
            d[a] += 1
    return d


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = []
    for i in range(Q):
        BC.append(tuple(map(int, input().split())))

    d = create_dict(A)

    ans = sum_dict(d)
    for b, c in BC:
        db = d.get(b)
        if db is None:
            db = 0
        if d.get(c) is None:
            d[c] = 0
        d[c] += db
        d[b] = 0

        ans += (c - b) * db
        print(ans)
