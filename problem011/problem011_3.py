#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B

x, y = map(int, input().split())

if y > x:
	w = y
	y = x
	x = w

while y > 0:
	amari = x % y
	x = y
	y = amari

print(x)