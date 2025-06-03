import sys
read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    S = readline().decode('utf-8').strip()
    ans = 0
    for i in range(10):
        x = S.find(str(i), 0, N - 2)
        if x != -1:
            for j in range(10):
                y = S.find(str(j), x + 1, N - 1)
                if y != -1:
                    for k in range(10):
                        z = S.find(str(k), y + 1, N)
                        if z != -1:
                            ans += 1
    print(ans)
if __name__ == '__main__':
    main()
