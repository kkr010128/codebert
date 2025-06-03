import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    a, b, c, k = map(int, input().split())
    r = min(k, a)
    k -= a
    if k > 0:
        k -= b
        if k > 0:
            r -= k
    print(r)

if __name__ == '__main__':
    main()
