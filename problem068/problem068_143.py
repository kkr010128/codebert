#def area###############################
def pr(s,a,b):
	print s[int(a):int(b)+1]

def rv(s,a,b):
#	a="abcdefghijklmn"len=14
#	ra="nmlkjihgfedcba"
#		edc=9,10,11
#	ans="abedcfghijklmn"
#	reverse 2 4
#	14-b-1,14-a-1
#	"
	tmp=s[::-1]
	news=s[:int(a)]+tmp[len(tmp)-int(b)-1:len(tmp)-int(a)]+s[int(b)+1:]
	return news
def rp(s,a,b,p):
	news=s[:int(a)]+p+s[int(b)+1:]
	return news
########################################


I=raw_input()
n=int(input())
for i in range(n):
	k=raw_input().split(" ")
	if k[0]=="replace":
		I=rp(I,k[1],k[2],k[3])
	elif k[0]=="reverse":
		I=rv(I,k[1],k[2])
	elif k[0]=="print":
		pr(I,k[1],k[2])