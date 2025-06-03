import sys
numbers = []
for line in sys.stdin:
	numbers.append(int(line))

k = []
k.append(1)
k.append(1)

def getFib(i, n):
    if i == n :
        print(k[-1])
        return
    k.append(int(k[i - 1]) + int(k[i - 2]))
    getFib(i + 1, n)

getFib(2, int(numbers[0])+1)
