def subset_sum(s, a):
	dict = {}
	return subset_rec(0, s, a, dict)
	
def subset_rec(i, s, a, dict):
	key = str(i) + '-' + str(s)
	ret = False
	if key in dict:
		ret = dict[key]
	elif s == 0:
		ret = True
	elif i >= len(a):
		ret =  False
	else:
		ret = subset_rec(i+1, s-a[i], a, dict) or subset_rec(i+1, s, a, dict)
	dict[key] = ret
	return ret	

n = int(input())
a = list(map(int, input().split()))
p = int(input())
q = list(map(int, input().split()))
for i in range(p):
	if subset_sum(q[i], a):
		print('yes')
	else:
		print('no')

