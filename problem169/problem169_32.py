import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    A = LI()
    sub = [0]*n
    for a in A:
        sub[a-1] += 1
    for s in sub:
        print(s)

if __name__ == '__main__':
    main()