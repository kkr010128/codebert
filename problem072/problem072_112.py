import sys

input = sys.stdin.readline

def main():
    ans = 'No'
    N = int(input())
    c = 0
    for _ in range(N):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            c += 1
            if c >= 3:
                ans = 'Yes'
                break
        else:
            c = 0

    print(ans)

if __name__ == '__main__':
    main()