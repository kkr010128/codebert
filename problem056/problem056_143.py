if __name__ == "__main__":

    n, m = map(int, raw_input().split())

    b = [0] * m
    A = [0] * m * n

    for i in xrange(n):
        A[i*m:i*m+m] = map( int, raw_input().split())

    for i in xrange(m):
        b[i] = int(raw_input())

    c = [0] * n
    for i in xrange(n):
        for j in xrange(m):
            c[i] += A[i*m + j] * b[j]

    for i in xrange(n):
        print c[i]