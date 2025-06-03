import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    r = 0
    for i1 in range(1, n+1):
        for i2 in range(1, n+1):
            if i1 * i2 >= n:
                break
            else:
                r += 1
    print(r)

if __name__ == '__main__':
    main()
