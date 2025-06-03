import math
n=input()
S=100000

for i in range(n):
	S*=1.05
	S=int( math.ceil(S/1000)*1000 )
print S
