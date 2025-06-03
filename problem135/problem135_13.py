A,B = input().split()
A = int(A)
B = int(B[0])*100 + int(B[2])*10 + int(B[3])
ans = A*B
ans //= 100
print(ans)