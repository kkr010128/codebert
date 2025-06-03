w = raw_input()

words = []
while True:
	line = raw_input()
	if line == "END_OF_TEXT":
		break
	else:
		line_list = line.split(" ")
		words += line_list
#print words

cnt = 0
for word in words:
	if w.lower() == word.lower():
		cnt += 1
print cnt