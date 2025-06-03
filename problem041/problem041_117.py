W,H,x,y,r = map(int, raw_input().split(" "))
result = ""
if x-r < 0 or y-r < 0:
	result = "No"
elif x+r > W or y+r > H:
	result = "No"
else:
	result = "Yes"
print result