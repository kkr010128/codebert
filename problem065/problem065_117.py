W = raw_input().upper()
T = []
while True:
	txt = raw_input()
	if txt == "END_OF_TEXT":
		break
	T += txt.upper().split()
print T.count(W)