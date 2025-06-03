N=int(input())
array=[int(x) for x in input().split()]
answer=0
for i in array:
	answer=answer^i
tobeprinted=[answer^i for i in array]
print(*tobeprinted)