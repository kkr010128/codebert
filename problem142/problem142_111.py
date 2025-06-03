import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = str(readline().rstrip().decode('utf-8'))
    d = {"2": "hon", "4": "hon", "5": "hon", "7": "hon", "9": "hon", "0": "pon", "1": "pon", "6": "pon", "8": "pon", "3": "bon"}
    print(d[n[-1]])


if __name__ == '__main__':
    solve()
