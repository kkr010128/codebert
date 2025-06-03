X = input()

ans = "1"
if int(X) < 100:
	ans = "0"
elif not int(X[:-2])*5 >= int(X[-2:]):
	ans = "0"

print(ans)


