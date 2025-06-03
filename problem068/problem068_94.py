def str_reverse(s, a, b):
    s_new = s[0:a]
    s_rev = s[a:b+1]
    s_rev_len = len(s_rev)
    for i in range(s_rev_len):
        j = s_rev_len - i - 1
        s_new += s_rev[j]
    s_new += s[b+1:]
    return s_new

def str_replace(s, a, b, new):
    s_new = s[0:a]
    s_new += new
    s_new += s[b+1:]
    return s_new


s = input()
n = int(input())
for q in range(n):
    line = input()
    if line.find('print') == 0:
        cmd, a, b  = line.split()
        a = int(a)
        b = int(b)
        print(s[a:b+1])

    elif line.find('reverse') == 0:
        cmd, a, b  = line.split()
        a = int(a)
        b = int(b)
        s = str_reverse(s, a, b)

    elif line.find('replace') == 0:
        cmd, a, b, p  = line.split()
        a = int(a)
        b = int(b)
        s = str_replace(s, a, b, p)