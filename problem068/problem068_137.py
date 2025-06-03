def s_print(s, line):
    a, b = map(int, line.split()[1:])
    print(s[a:b + 1])
    return s


def s_reverse(s, line):
    a, b = map(int, line.split()[1:])
    return s[:a] + s[a:b + 1][::-1] + s[b + 1:]


def s_replace(s, line):
    ls = line.split()
    a, b = map(int, ls[1:3])
    rep = ls[-1]
    return s[:a] + rep + s[b + 1:]


func_dict = {'pri': s_print, 'rev': s_reverse, 'rep': s_replace}

s, q = input(), int(input())
while q:
    line = input()
    s = func_dict[line[:3]](s, line)
    q -= 1