A,B = map(str,input().split())
A = int(A)
B1 = int(B[0])
B2 = int(B[-2])
B3 = int(B[-1])

ans = A*(100*B1+10*B2+B3)//100
print(int(ans))