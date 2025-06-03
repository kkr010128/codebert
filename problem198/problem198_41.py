n = int(input())

l = []


def f(n):
    return chr(n+ord("a"))


def search(s: str, cnt: int) -> str:
    if len(s) == n:
        return s
    cnt = len(set(list(s)))
    for i in range(0, min(cnt, len(s)) + 1):
        g = search("".join([s, f(i)]), cnt + max(0, i - len(s) + 1))
        if g is not None:
            l.append(g)


search("", 1)

l.sort()

for s in l:
    print(s)
