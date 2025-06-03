def main():
    n, k, c = map(int, input().split())
    s = input()

    def f(r):
        interval = 0
        count = k
        for i in r:
            if count == 0:
                break
            if interval > 0:
                interval -= 1
                continue
            if s[i] == 'o':
                yield i
                count -= 1 
                interval = c

    for i, j in zip(f(range(0, n)), reversed(list(f(range(n-1, -1, -1))))):
        if i == j:
            yield str(i+1)


print("\n".join(main()))