one_word = raw_input()
word_count = 0
word_list = []

while 1:
	temp = raw_input()
	word_list += temp.split()
	
	if word_list[len(word_list)-1] == "END_OF_TEXT":
		break

for word in word_list:
	if one_word.lower() == word.lower():
		word_count += 1

print word_count