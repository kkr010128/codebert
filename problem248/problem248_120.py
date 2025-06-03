#入力:N,M(int:整数)
def input2():
	return map(str,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))





s,t=input2()

print("{}{}".format(t,s))