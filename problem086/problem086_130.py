inputValue=input()

l=inputValue.split(" ")
N=int(l[0])
X=int(l[1])
T=int(l[2])
num=0
num= int((N/X))*T
if N%X >0:
	num=num+T

print (num)