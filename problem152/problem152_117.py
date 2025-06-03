def to_lines(s):
    h = 0
    b = 0
    for c in s:
        if c == '(':
            h += 1
        else:
            h -= 1
        b = min([b, h])
    return (b, h)


def check(lines):
    h = 0
    for line in lines:
        if h + line[0] < 0:
            return False
        h += line[1]
    return True


def main():
    N = int(input())
    up_lines = list()
    down_lines = list()
    total = 0
    for _ in range(N):
        line = to_lines(input())
        total += line[1]
        if line[1] >= 0:
            up_lines.append(line)
        else:
            inv_line = (line[0] - line[1], -line[1])
            down_lines.append(inv_line)
    up_lines.sort(key=lambda x: x[0], reverse=True)
    down_lines.sort(key=lambda x: x[0], reverse=True)
    if total == 0 and check(up_lines) and check(down_lines):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()