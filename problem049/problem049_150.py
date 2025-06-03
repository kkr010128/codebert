def solve(h, w):
    line = ''.join(['#' for i in range(w)])
    [print(line) for i in range(h)]
    print()

if __name__ == '__main__':
    while True:
        h, w = [int(i) for i in input().split()]
        if h == w == 0: break
        solve(h, w)