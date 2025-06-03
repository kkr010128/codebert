a,b,c,d = map(int,input().split())
t_deth=(a+d-1)//d
a_deth=(c+b-1)//b
if t_deth>=a_deth:
	print('Yes')
else:
	print('No')