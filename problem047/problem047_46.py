while True:
    a,op,b=input().split()
    if op=='?': break
    eval("print( int(int(a) {0} int(b)) )".format(op))
