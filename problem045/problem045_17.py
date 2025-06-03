if __name__ == "__main__":
	a, b = map( int, input().split() )
	print("%d %d %.5f"%(int(a/b),a%b,float(a/b)))