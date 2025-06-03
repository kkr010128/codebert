dic = set()
n = int(input())
for i in range(n):
	s = input()
	if s[0] == 'i': 
	    dic.add(s[7:])
	    
	else: print("yes" if s[5:] in dic else "no")
