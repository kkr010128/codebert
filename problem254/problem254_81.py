import sys

def solve():
    input = sys.stdin.readline
    A = int(input())
    B = int(input())
    C = list(set([1, 2, 3]) - set([A, B]))
    print(C[0])

    return 0

if __name__ == "__main__":
    solve()