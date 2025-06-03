#create date: 2020-07-03 10:10

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    a, b, c, k = na()
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    else:
        print(a-(k-(a+b)))

if __name__ == "__main__":
    main()