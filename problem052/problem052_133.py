def CheckNum(n, x, i):
	x = i
	if x % 3 == 0:
		print(" %d"%(i), end="")
		return 2, i, x
	return 1, i, x

def Include3(n, x, i):
	if x % 10 == 3:
		print(" %d"%(i), end="")
		return 2, i, x
	x = int(x/10)
	if x != 0:
		return 1, i, x
	return 2, i, x

def EndCheckNum(n, x, i):
	i += 1
	if i <= n:
		return 0, i, x
	print("")
	return 3, i, x
	
def call(n):
	counter = 0
	i = 1
	x = 1
	func = [CheckNum, Include3, EndCheckNum]
	while counter != 3:
		counter, i, x = func[counter](n, x, i)

n = int(input())
call(n)