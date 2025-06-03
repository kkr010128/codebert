A,V = map(int,input().split())
B,W = map(int,input().split())

T = int(input())

dist = abs(A-B)
diff = V-W
if dist > diff * T:
	print("NO")
else:
	print("YES")