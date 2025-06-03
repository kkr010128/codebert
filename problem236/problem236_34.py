import sys
def main():
    h, w, n = map(int, sys.stdin.read().split())
    print(-(-n // max(h, w)))

if __name__ == '__main__':
    main()
