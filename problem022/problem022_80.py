n=int(input())
S=input().split(' ')
q=int(input())
T=input().split(' ')

def equal_element(S,T):
	m=0
	for i in range(len(T)):
		for j in range(len(S)):
			if S[j]==T[i]:
				m+=1
				break
	return(m)
	
print(equal_element(S,T))
