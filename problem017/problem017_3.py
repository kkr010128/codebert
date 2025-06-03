# coding: utf-8

cnt = int()
m = int()
g = []

def insersion_sort(a, n, g):
    global cnt
    for i in xrange(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j = j - g
            cnt += 1
        a[j+g] = v
    return list(a)

def shell_sort(a, n):
    global cnt
    global m
    global g
    cnt = 0
    m = 0
    g = []
    nn = n
    while True:
        nn /= 2
        if nn <= 0:
            break
        g.append(nn)
        m += 1
    if n == 1:
        m = 1
        g = [1]
    for i in g:
        a = insersion_sort(a, n, i)
    return a

def main():
    global cnt
    global m
    global g
    n = input()
    a = []
    for i in xrange(n):
        a.append(input())
    a = shell_sort(a, n)
    print m
    print " ".join(map(str, g))
    print cnt
    for i in xrange(n):
        print a[i]

main()