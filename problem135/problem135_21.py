A,B = map(str,input().split())
A = int(A)
B = int(B[0])*100+int(B[2])*10+int(B[3])
print(int(A*B//100))