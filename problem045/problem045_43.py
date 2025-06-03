a,b = list(map(int, input().split()))
d = int(a / b)
r = int(a % b)
f = a / b
print(str(d) + " " + str(r) + " " + str("{0:.10f}".format(f)))