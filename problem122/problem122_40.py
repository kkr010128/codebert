from collections import Counter


def solve(string):
    n, *aqbc = map(int, string.split())
    a, _, bc = aqbc[:n], aqbc[n], aqbc[n + 1:]
    s = sum(a)
    t = Counter(a)
    ans = []
    for b, c in zip(*[iter(bc)] * 2):
        if b in t.keys():
            s += (c - b) * t[b]
            t[b], t[c] = 0, t[b] + t[c]
        ans.append(s)
    return "\n".join(map(str, ans))


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
