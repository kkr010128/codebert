def solve(h, w):
    odd_line = '#.' * (w // 2)
    even_line = '.#' * (w // 2)
    if w%2:
        odd_line = odd_line + '#'
        even_line = even_line + '.'
    two_lines = odd_line + '\n' + even_line + '\n'
    print(two_lines * (h // 2), end='')
    if h%2:
        print(odd_line)
    print()

if __name__ == '__main__':
    while True:
        h, w = [int(i) for i in input().split()]
        if h == w == 0: break
        solve(h, w)