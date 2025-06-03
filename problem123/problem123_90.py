import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())
    allxor = a[0]
    for ae in a[1:]:
        allxor = allxor ^ ae
    for ae in a:
        print(allxor ^ ae, end = ' ')

if __name__ == '__main__':
    main()