def main():
    n, x, y = map(int, input().split())
    distances = [0 for _ in range(n)]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            distances[min(j-i, min(abs(i-x)+abs(j-y), abs(j-x)+abs(i-y))+1)] += 1

    for v in distances[1:]:
        print(v)


if __name__ == '__main__':
    main()
