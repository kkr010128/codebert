a = []
while True:
    m,n,o = input().split()
    m=int(m)
    o=int(o)
    if n == "?":
        break
    if n=="+":
    	a.append(m+o)
    elif n=="-":
    	a.append(m-o)
    elif n=="*":
    	a.append(m*o)
    elif n=="/":
    	a.append(int(m/o))
 

for i in a:
	print(i)