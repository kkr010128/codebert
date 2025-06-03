nb = int(input())
sentence = input()

if len(sentence) > nb:
	print(sentence[0:nb] + '...')
else:
	print(sentence)