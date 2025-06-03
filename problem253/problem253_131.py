import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, a, b = MI()
    d = b - a
    ans = 0
    if d%2:
        temp = min(a-1, n-b)
        ans = (d-1)//2 + temp + 1
    else:
        ans = d//2
    print(ans)

if __name__ == '__main__':
    main()