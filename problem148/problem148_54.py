def main(a, b,c,k):

    m = 0
    if k <=a:
        m = k
    elif k <=(a+b):
        m = a
    elif k <= a+b+c:
        m = (a-(k-(a+b)))
    return m
a, b, c , k = map(int, input().split())
print(main(a,b,c,k))