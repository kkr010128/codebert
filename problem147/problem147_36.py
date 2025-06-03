#create date: 2020-07-03 10:09

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    s = ns()
    t = ns()
    print("Yes" if s==t[:-1] else "No")

if __name__ == "__main__":
    main()