from collections import deque


def solver(K):
    q = deque([i for i in range(1, 10)])

    if K <= 9:
        ans = q[K - 1]

    else:
        cnt = 9
        for i in range(1, K):
            c = q.popleft()

            if c % 10 != 0:
                q.append(c * 10 + (c % 10) - 1)
                cnt += 1
                if cnt >= K:
                    break

            q.append(c * 10 + (c % 10))
            cnt += 1
            if cnt >= K:
                break

            if c % 10 != 9:
                q.append(c * 10 + (c % 10) + 1)
                cnt += 1
                if cnt >= K:
                    break

        ans = q[-1]
    return ans


def run():
    K = int(input())
    ans = solver(K)

    print(ans)


run()
