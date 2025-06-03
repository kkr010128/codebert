if __name__ == "__main__":
    t0 = int(raw_input())
    h = t0 / 60 / 60
    t1 = t0 - ( h * 60 * 60 )
    m = t1  / 60
    s = t1 - ( m * 60 )
    print "{0}:{1}:{2}".format(h,m,s)