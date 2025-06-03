n = input()

dict_ = set()
for _ in xrange(n):
    cmd, str_ = raw_input().split()
    if cmd == "insert":
        dict_.add(str_)
    elif cmd == "find":
        if str_ in dict_:
            print "yes"
        else:
            print "no"