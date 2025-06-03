import sys

#fin = open("test.txt", "r")
fin = sys.stdin

sentence = fin.read()
sentence = sentence.lower()

num_alphabet_list = [0 for i in range(26)]

for c in sentence:
	if ord(c) < ord('a') or ord(c) > ord('z'):
		continue

	num_alphabet_list[ord(c) - ord('a')] += 1

for i in range(0, 26):
	print(chr(i + ord('a')), end="")
	print(" : ", end="")
	print(num_alphabet_list[i])