from sys import stdin
input = stdin.readline

def solve():
    N = int(input())
    res = []
    while True:
        N -= 1
        N,r = divmod(N,26)
        res.append(chr(ord('a')+r))
        if N == 0:
            break

    print(''.join(reversed(res)))






if __name__ == '__main__':
    solve()
