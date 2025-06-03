word = input()
start = 0
end = len(word)
while(True):
	i = word.find('?', start, end)
	if (i == -1):
		break
	elif (i == (end-1)):
		word = word.replace('?', "D", 1)   
	elif (word[i-1] == 'P'):
		word = word.replace('?', "D", 1)
	elif ((word[i+1] == "?") or (word[i+1] == "D")):
		word = word.replace('?', "P", 1)
	else:
		word = word.replace('?', "D", 1)
	start = i + 1
print(word)