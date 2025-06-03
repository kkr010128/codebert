import heapq
def main():
    X, Y, A, B, C = (int(_) for _ in input().split())
    p = sorted([int(_) for _ in input().split()])[::-1]
    q = sorted([int(_) for _ in input().split()])[::-1]
    r = sorted([int(_) for _ in input().split()])[::-1]
    output = 0
    apple = list()
    heapq.heapify(apple)
    for i in range(X):
        heapq.heappush(apple, p[i])
        output += p[i]
    for i in range(Y):
        heapq.heappush(apple, q[i])
        output += q[i]
    i = 0
    while i < C:
        x = heapq.heappop(apple)
        if x < r[i]:
            heapq.heappush(apple, r[i])
            output = output - x + r[i]
            i += 1
        else: break

    print(output)
    return

if __name__ == '__main__':
    main()
