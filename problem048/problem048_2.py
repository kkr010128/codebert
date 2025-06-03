if __name__ == "__main__":
	input()
	lis = [ int(i) for i in input().split()]
	print("%d %d %d"%(min(lis),max(lis),sum(lis)))