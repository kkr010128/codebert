A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())
 
if A < B:
	if A + (V*T) >= B + (W*T):
		print("YES")
	else:
		print("NO")
else:
	if A - (V*T) <= B - (W*T):
		print("YES")
	else:
		print("NO")