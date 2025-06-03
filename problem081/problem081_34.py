a = input().split()
dist = int(a[0])
time = int(a[1])
speed = int(a[2])
if(speed * time < dist):
	print("No")
else:
	print("Yes")