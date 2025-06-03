while 1:
    a, op, b = raw_input().split(' ')
    if op == '?':break
    print eval("%s %s %s"%(a, op, b))