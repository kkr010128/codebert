W = input().lower()

T = []
while True:
	R = input()
	if R == "END_OF_TEXT":
		break
	R = R + " "
	T.append(R)

T = (''.join(T)).lower()
T = T.split()
print(T.count(W))