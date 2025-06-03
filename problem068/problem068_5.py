import sys

def reverse(str, a, b):
	head = str[0:a]
	tail = str[b + 1:]
	mid = str[a:b + 1]
	reversed_str = head + mid[::-1] + tail
	return reversed_str

def replace(str, a, b, rstr):
	head = str[0:a]
	tail = str[b + 1:]
	replaced_str = head + rstr + tail
	return replaced_str


#fin = open("test.txt", "r")
fin = sys.stdin

str = fin.readline()
q = int(fin.readline())

for i in range(q):
	query_list = fin.readline().split()
	op = query_list[0]
	a = int(query_list[1])
	b = int(query_list[2])

	if op == "print":
		print(str[a:b + 1])
	elif op == "reverse":
		str = reverse(str, a, b)
	else:
		str = replace(str, a, b, query_list[3])