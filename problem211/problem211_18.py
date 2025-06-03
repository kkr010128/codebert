def input_num():
	ls = input().strip().split(" ")
	return [int(e) for e in ls]

n,r = input_num()
if n >= 10:
	print(r)
else:
	print(r+100*(10-n))
