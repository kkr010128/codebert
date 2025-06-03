import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n = int(input())
    r = []
    while n > 0:
        n -= 1
        t1 = n % 26
        r.append(chr(t1+97))
        n = n // 26
    r2 = "".join(r[::-1])
    print(r2)

if __name__ == '__main__':
    main()