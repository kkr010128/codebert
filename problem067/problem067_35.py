t=0
h=0
n=input()
for _ in range (n):
	s = raw_input().split()
	if s[0] > s[1]:
		t+=3
	elif s[0] < s[1]:
		h+=3
	else:
		t+=1
		h+=1
print str(t) + " " + str(h)
