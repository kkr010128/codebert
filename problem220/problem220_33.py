
if __name__ == '__main__':

	tmp0 = input().split()
	tmp1 = map(int,input().split())
	tmp2 = input()

	dic = {}

	for x,y in zip(tmp0,tmp1):
		dic[x] = y

	dic[tmp2] = dic[tmp2] - 1

	print(*dic.values())

