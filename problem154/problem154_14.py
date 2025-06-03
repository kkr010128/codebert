import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    n, k = map(int, input().split())
    sunuke = [0] * n
    for _ in range(k):
        d = int(input())
        a = tuple(map(int, input().split()))
        for ae in a:
            sunuke[ae-1] += 1

    r = sunuke.count(0)
    print(r)

if __name__ == '__main__':
    main()
