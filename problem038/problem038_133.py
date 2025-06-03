a,b = map(int, raw_input().split(" "))
result = ""
if a < b:
	result = "a < b"
elif a > b:
	result = "a > b"
else:
	result = "a == b"
print result