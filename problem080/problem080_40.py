from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())


def main():
    N = i_input()
    Z = []
    W = []
    for i in range(1, N + 1):
        x, y = i_map()
        Z.append(x + y)
        W.append(x - y)
    Z.sort()
    W.sort()
    ans = max([Z[-1] - Z[0], W[-1] - W[0]])
    print(ans)

if __name__ == "__main__":
    main()
