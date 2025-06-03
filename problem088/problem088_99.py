import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
def main():
    n, *a = map(int, read().split())
    r = 0
    maxtall = a[0]
    for i1 in range(1, n):
        if a[i1] > maxtall:
            maxtall =  a[i1]
        else:
            r += maxtall - a[i1]
    print(r)

if __name__ == '__main__':
    main()
