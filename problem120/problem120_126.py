import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, k, *p = map(int, read().split())
    p.sort()
    r = sum(p[:k])
    print(r)

if __name__ == '__main__':
    main()
