S=list(input())
T=list(input())
T.pop(len(T)-1)
if S == T:
	print("Yes")
else:
	print("No")