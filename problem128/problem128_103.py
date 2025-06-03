import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    x, n, *p = map(int, read().split())
    sa = 10000
    r = 10000
    for i1 in range(-101, 202):
        if i1 not in p:
            if abs(x - i1) < sa:
                sa = abs(x - i1)
                r = i1
    print(r)

if __name__ == '__main__':
    main()
