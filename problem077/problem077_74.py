a, b, c, d = input().split() 
a = int(a)
b = int(b)
c = int(c)
d = int(d)
xy1 = a*c
xy2 = a*d
xy3 = b*c
xy4 = b*d
 
print(max([xy1, xy2, xy3, xy4]))