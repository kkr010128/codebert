from string import ascii_lowercase, ascii_uppercase
l = ascii_lowercase
u = ascii_uppercase
def conv(c):
    if c in l:
        return u[l.index(c)]
    if c in u:
        return l[u.index(c)]
    return c
open(1, 'w').write("".join(map(conv, open(0).readline())))
