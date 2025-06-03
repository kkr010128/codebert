String = input()
A=input()
String+=String[0:len(A)]
#print(String)
for i in range(len(String)-len(A)+1):
	if String[i:i+len(A)] == A:
		print("Yes")
		break
else: print("No")