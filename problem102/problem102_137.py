# C - Marks


def marks(n, k, a):
    results = []
    for i in range(n - k):
        if a[i] < a[i + k]:
            results.append("Yes")
        else:
            results.append("No")
    return results


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    results = marks(n, k, a)
    for i in results:
        print(i)
