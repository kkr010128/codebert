a = input()
a = int(a)
h = a//3600
m = (a-3600*h)//60
s = (a-3600*h-60*m)
print(str(h)+':'+str(m)+':'+str(s))
