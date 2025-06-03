N,A,B = map(int,input().split())

kotae= N//(A+B)*A
am = N%(A+B)

if am>A:
	am=A

print(kotae+am)