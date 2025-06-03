def solve(string):
    _, *l = map(int, string.split())
    l.sort()
    ans = 0
    for i, l0 in enumerate(l[:-2]):
        for j, l1 in enumerate(l[i + 1:-1]):
            if l0 == l1:
                continue
            for l2 in l[i + j + 2:]:
                if l1 == l2:
                    continue
                if l2 < l0 + l1:
                    ans += 1
                else:
                    break
    return str(ans)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read().strip()))
