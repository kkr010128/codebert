def main():

	numbers = input().split()
	a, b, c = map(int, numbers)

	a_to_b = list(range(a, b + 1))    #a to b
	result = [x for x in a_to_b if c % x == 0]
	#約数検索
	count = int(len(result))
	print(count)
	


if __name__=="__main__":
	main()