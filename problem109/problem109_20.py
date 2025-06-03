from sys import stdin

input = stdin.readline
from collections import Counter

def solve():
    n = int(input())
    verdict = [ inp for inp in stdin.read().splitlines()]
    c = Counter(verdict)
    print(f'AC x {c["AC"]}')
    print(f'WA x {c["WA"]}')
    print(f'TLE x {c["TLE"]}')
    print(f'RE x {c["RE"]}')


if __name__ == '__main__':
    solve()
