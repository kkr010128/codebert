x = input()
x = x.split(" ")
x = [int(z) for z in x]
print("%d %d %f" % (x[0]//x[1], x[0]%x[1], x[0]/x[1]))