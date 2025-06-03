a,b = list(map(int, input().split()))
c = int(a / b)
d = a % b
e = a / b

print(str(c) + " " + str(d) + " "+"{0:.8f}".format(e))