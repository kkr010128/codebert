a,b = list(map(int, input().split()))
d = int(a / b)
r = a % b
f = a / b
print(str(d) + " "+ str(r) + " "+ "{0:.20f}".format(f))