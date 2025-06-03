n, r= input().split()
n, r= int(n), int(r)
eq=r
if n < 10:
	eq=0
	eq= r+(100*(10-n))

print(eq)
