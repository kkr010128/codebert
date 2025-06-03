import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, m = map(int, input().split())
    h = tuple(map(int, input().split()))
    edges = {e:[] for e in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(h[b])
        edges[b].append(h[a])
    r = 0
    for i, he in enumerate(h):
        if not edges[i]:
            r += 1
        else:
            r += he > max(edges[i])

    print(r)
if __name__ == '__main__':
    main()