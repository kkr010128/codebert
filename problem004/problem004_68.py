def main():
	n = int(input())

	for _ in range(n):
		len_list = map(int, input().split())
		check_tri(len_list)

def check_tri(len_list):
	import itertools
	import math

	flag = False
	for tmp in list(itertools.permutations(len_list)):
		if (pow(tmp[0], 2) + pow(tmp[1], 2)) == pow(tmp[2], 2):
			flag = True
			break

	if flag == True:
		print('YES')
	else:
		print('NO')

if __name__ == '__main__':
	main()