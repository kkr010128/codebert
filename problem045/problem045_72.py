x = input().split()

x_int = [int(i) for i in x]
d = x_int[0]//x_int[1]
r = x_int[0] % x_int[1]
f = (x_int[0]) / (x_int[1])
print('{0} {1} {2:f}'.format(d,r,f))