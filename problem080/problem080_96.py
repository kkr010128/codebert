def main():
    N = int(input())
    points = [None] * N
    for i in range(N):
        x, y = map(int, input().split())
        points[i] = (x, y)
    ans = 0
    points.sort(reverse=True)
    topright = points[0][0] + points[0][1]
    bottomright = points[0][0] - points[0][1]
    for i in range(N):
        tr = points[i][0] + points[i][1]
        br = points[i][0] - points[i][1]
        ans = max([ans, abs(topright - tr), abs(bottomright - br)])
        topright = max(topright, tr)
        bottomright = max(bottomright, br)
    print(ans)


if __name__ == "__main__":
    main()
