from collections import deque
def main():
    k = int(input())
    d = deque(list(range(1, 10)))
    ans = 0
    for _ in range(k):
        ans = d.popleft()
        if ans % 10 != 0:
            d.append(10 * ans + (ans % 10) - 1)
        d.append(10 * ans + (ans % 10))
        if ans % 10 != 9:
            d.append(10 * ans + (ans % 10) + 1)
    print(ans)


if __name__ == '__main__':
    main()
