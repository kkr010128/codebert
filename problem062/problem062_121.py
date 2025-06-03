readline = open(0).readline
write = open(1, 'w').write
while 1:
    x = readline()
    if x == "0\n":
        break
    write("%d\n" % sum(map(int, x.strip())))
