input_line = input().split()
a = int(input_line[0])
b = int(input_line[1])
if a > b:
	symbol = ">"
elif a < b:
	symbol = "<"
else:
	symbol = "=="
print("a",symbol,"b")