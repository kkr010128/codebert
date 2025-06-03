import sys
def main():
    n, m = map(int, input().split())
    r = n * (n - 1) / 2
    r += m * (m - 1) / 2
    print(int(r))

if __name__ == '__main__':
    main()
