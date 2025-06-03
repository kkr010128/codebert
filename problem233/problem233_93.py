import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())

    r = 0
    minp = a[0]
    for i1 in range(n):
        if minp >= a[i1]:
            r += 1
            minp = a[i1]

    print(r)

if __name__ == '__main__':
    main()
