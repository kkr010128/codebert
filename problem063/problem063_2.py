import sys

alp=[]
for i in range(97,97+26):
	alp.append(chr(i))

s=sys.stdin.read().lower()

for i in alp:
	num=0
	for j in s:
		if i==j:
			num+=1
	print(i+' : '+str(num))

