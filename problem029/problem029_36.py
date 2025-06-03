x1,y1,x2,y2 = map(float,input().split())
an = (x1 - x2)**2 + (y1 - y2)**2
dis = an/2
v = an/4
while abs(dis**2 - an) > 0.0001:
	if dis**2 > an:
		dis -= v
	else:
		dis += v
	v = v/2
print(dis)
