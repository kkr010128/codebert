def prod(int_list):
	p = 1
	for i in int_list:
		p *= i
	return p
	
int_ary = [int(s) for s in input().split(" ")]
print(prod(int_ary), 2 * sum(int_ary))