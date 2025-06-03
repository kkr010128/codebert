if __name__ == "__main__":

    n = int(raw_input())
    v = map( int, raw_input().split())

    min = 1000000
    max = -1000000
    s = 0
    i = 0
    while i < n:
       if min > v[i]:
           min = v[i]
       if max < v[i]:
           max = v[i]
       s += v[i]
       i += 1

    print "{0} {1} {2}".format( min, max, s)