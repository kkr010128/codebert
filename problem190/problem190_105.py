
def solve():
	s=input()
	if(len(s)%2==0):
		print("No")
		return 
	else :
		n=len(s)//2
		str1=s[:n]
		str2=s[n+1:]
		# print(str1,str2)
		if(str1==str2):
			print("Yes")
		else:
			print("No")
if __name__ == "__main__":
	solve()