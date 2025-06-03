# (+1,+2)をn回，(+2,+1)をm回とすると
#  n + 2m = X
# 2n +  m = Y でn,mが求まる．
# このとき答えは(n+m)Cn通り

def combination(n,r):
	"""
    高速な組み合わせの計算．
	nCrは必ず整数になるため分母を全部約分で1にしてから残った分子の積を求める．
	[参考]https://kadzus.hatenadiary.org/entry/20081211/1229023326
    """

	if n-r < r: r = n-r
	if r == 0: return 1
	if r == 1: return int(n)

	numerator = [i+1 for i in range(n-r, n)]
	denominator = [i+1 for i in range(r)]

	for p in range(2,r+1):
		pivot = denominator[p-1]
		if pivot > 1:
			offset = (n-r)%p
			for k in range(p-1, r, p):
				numerator[k-offset] /= pivot
				denominator[k] /= pivot
	
	ans = 1
	for i in range(r):
		if numerator[i] > 1:
			ans *= numerator[i]
			if ans >= 1e9+7: ans %= 1e9+7
	
	return int(ans)

X,Y = map(int, input().split())

if (X+Y)%3 != 0:
	ans = 0
else:
	n = int((2*Y-X)/3)
	m = int(Y-2*n)
	if n<0 or m<0:
		ans = 0
	else:
		ans = combination(n+m, n)

print(ans)