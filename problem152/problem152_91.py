import sys
input=sys.stdin.readline
n=int(input())
cnt=[]
for i in range(n):
	s=input().rstrip()
	l=s.count("(")
	r=s.count(")")
	minus=0
	now=0
	for j in range(len(s)):
		if s[j]=="(":
			now+=1
		else:
			now-=1
			minus=min(minus,now)
	cnt.append((l,r,s,minus))
cnt.sort(key=lambda x:x[1]-x[0])
plus=[]
minus=[]
#x[3]は最小値　x[0]-x[1]が合計値
for x in cnt:
	if x[0]-x[1]>0:
		plus.append(x)
	else:
		minus.append(x)
plus.sort(key=lambda x:-x[3])#最小値の少ない(0に近い方から)
minus.sort(key=lambda x:-(x[0]-x[1]-x[3]))
lr=0#l-r
for x in plus+minus:
	if lr+x[3]<0:
		print("No")
		exit()
	lr+=x[0]-x[1]
if lr==0:
	print("Yes")
else:
	print("No")
