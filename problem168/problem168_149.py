import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

def main():
    n, m, *a = map(int, read().split())
    suma = sum(a)
    if n < suma:
        print(-1)
    else:
        print(n - suma)

if __name__ == '__main__':
    main()
