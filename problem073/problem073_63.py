import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(readline())
    ans = 0
    for i in  range(1, N):
        ans += (N-1)//i
    print(ans)
if __name__ == '__main__':
    main()
