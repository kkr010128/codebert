from collections import deque


def main():
    N, D, A = map(int, input().split())
    enemies = [None] * N
    for i in range(N):
        enemies[i] = tuple(map(int, input().split()))
    enemies.sort()
    q = deque()
    cur = 0
    ans = 0
    for x, h in enemies:
        while len(q) and q[0][0] < x:
            cur -= q.popleft()[1]
        remain = max(h - cur * A, 0)
        tmp = -(-remain//A)
        q.append((x + 2 * D, tmp))
        ans += tmp
        cur += tmp
    print(ans)


if __name__ == "__main__":
    main()
