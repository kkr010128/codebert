def resolve():
    X, Y, A, B, C = list(map(int, input().split()))
    P = sorted(list(map(int, input().split())), reverse=True)
    Q = sorted(list(map(int, input().split())), reverse=True)
    R = sorted(list(map(int, input().split())), reverse=True)
    eatreds = P[:X]
    eatgreens = Q[:Y]
    import heapq
    heapq.heapify(eatreds)
    heapq.heapify(eatgreens)
    for r in R:
        smallred = heapq.heappop(eatreds)
        smallgreen = heapq.heappop(eatgreens)
        reddiff = r-smallred
        greendiff = r-smallgreen
        if reddiff < 0 and greendiff < 0:
            heapq.heappush(eatreds, smallred)
            heapq.heappush(eatgreens, smallgreen)
            break
        if reddiff > greendiff:
            heapq.heappush(eatreds, r)
            heapq.heappush(eatgreens, smallgreen)
        else:
            heapq.heappush(eatreds, smallred)
            heapq.heappush(eatgreens, r)
    print(sum(eatreds)+sum(eatgreens))


if __name__ == "__main__":
    resolve()