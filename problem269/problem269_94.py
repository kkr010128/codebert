import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

T1,T2 = map(int,readline().split())
A1,A2 = map(int,readline().split())
B1,B2 = map(int,readline().split())

P = (A1 - B1) * T1
Q = (A2 - B2) * T2
if P > 0:
	P *= -1
	Q *= -1
 
if P + Q < 0:
	print(0)
elif P + Q == 0:
	print("infinity")
else:
	S = (-P) // (P + Q)
	T = (-P) % (P + Q)
	if T != 0:
		print(S * 2 + 1)
	else:
		print(S * 2)