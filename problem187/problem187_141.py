from collections import defaultdict
def main():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    klist = defaultdict(int)
    for i in range(n):
        for j in range(i+1, n):
            if (i <= x and j <= x) or (y <= i and y <= j):
                k = j - i
                klist[k] += 1
            elif i <= x and x < j <= y:
                k = min(j - i, (x - i + y - j) + 1)
                klist[k] += 1
            elif i <= x and y <= j:
                k = (j - i) - (y - x) + 1
                klist[k] += 1
            else:
                k = min((j - i), ((i - x) + abs(y - j) + 1))
                klist[k] += 1
    for i1 in range(1, n):
        print(klist[i1])

if __name__ == '__main__':
    main()
