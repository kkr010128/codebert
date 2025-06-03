def dts():
	return list(map(int,input().split()))

d,t,s=dts()

if d>t*s:
    print("No")
else:
    print("Yes")
