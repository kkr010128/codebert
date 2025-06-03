from collections import deque

def main():
    n = int(input())
    V = [None]*(n+1)
    ans = [None]*(n+1)
    for i in range(1, n+1):
        _, _, *v = map(int, input().split())
        V[i] = v
    q = deque([1])
    ans[1] = 0
    while q:
        node = q.pop()
        d = ans[node]+1
        for v in V[node]:
            if ans[v] is None:
                ans[v] = d
                q.appendleft(v)
    print(1, 0)
    for i, distance in enumerate(ans[2:], 2):
        print(i, distance or -1)

if __name__ == "__main__":
    main()
