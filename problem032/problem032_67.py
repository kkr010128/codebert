from math import sqrt

#def area########################################

def Manhattan(x,y):
	D=0.0
	for i in range(n):
		D+=abs(x[i]-y[i])
	return D

def Euclid(x,y):
	D=0.0
	for i in range(n):
		D+=(x[i]-y[i])**2
	D=sqrt(D)
	return D

def Noname(x,y):
	D=0.0
	for i in range(n):
		D+=abs((x[i]-y[i])**3)
	D**=1.0/3
	return D

def Infinity(x,y):
	L=list()
	for i in range(n):
		L.append(abs(x[i]-y[i]))			
	return max(L)

#################################################


n=int(input())
x=map(float,raw_input().split(" "))
y=map(float,raw_input().split(" "))

print Manhattan(x,y)
print Euclid(x,y)
print Noname(x,y)
print Infinity(x,y)