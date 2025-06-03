s=""
import fileinput
a=fileinput.input()
for i in a:
	s+=i
s=list(s)
res=[0 for i in range(26)]
for i in s:
	if i.isalpha():
		i=i.lower()
		res[ord(i)-ord("a")]+=1

for i in range(26):
	s=chr(i+ord("a"))+" : "+str(res[i])
	print(s)