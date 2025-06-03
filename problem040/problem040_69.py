length = raw_input()
a, b, c = length.split()
  
a = int(a)
b = int(b)
c = int(c)
num = [a, b, c]
num.sort()
for i in range(len(num)):
    print num[i],