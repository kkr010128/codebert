def fibo(n):
	S=[1,1]
	s=1
	if n>1:
		for i in range(2,n+1):
			S.append(S[i-1]+S[i-2])
			s=S[i]
	return s

def main():
	if __name__=="__main__":
		n=input()
		print(fibo(n))

main()