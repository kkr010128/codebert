n = int(input())
inp = list(map(int,input().split()))
inp.reverse()
for i in range(n-1):
	print(inp[i]," ",sep="",end="")
print(inp[n-1])