A,B=list(map(int,input().split()))

def gcd(A, B):
	if B==0: return(A)
	else: return(gcd(B, A%B))

print(gcd(A,B))