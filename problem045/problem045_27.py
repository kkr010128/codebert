if __name__ == "__main__":
    v = map( int, raw_input().split())
    a = v[0]
    b = v[1]

    d = a / b
    r = a - ( d * b )
    s = (0.0 + a) / b
    print "{0:d} {1:d} {2:.5f}".format( d, r, s)