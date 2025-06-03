line = raw_input()
lis = line.split()
a = int(lis[0])
b = int(lis[1])
s = a * b
len = 2 * (a + b)
print str(s) + " " + str(len)