def partpall(s,n):
	if s!=s[::-1]:
		return False
	else:
		return True

def pall(s,n):
	if s!=s[::-1]:
		return False
	return partpall(s[n//2 +1 :],n) and partpall(s[:n//2 ],n)


# s=input("enter:")
s=input()
# print("sucess",s,s[::-1])
# revStr=s[::-1]
n=len(s)
# print(n)
if pall(s,n):
	print("Yes")
else:
	print("No")