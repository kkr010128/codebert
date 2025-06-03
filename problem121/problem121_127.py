n=int(input())
# n-=1
r=[]
while n:
	n-=1
	r.append(chr(ord('a')+n%26))
	n//=26
print(*r[::-1],sep='')