NN =input().split()
N =int(NN[0])
A = int(NN[1])
B = int(NN[2])
X =A+B
Y =N//X
Z = N%X

if Z >=A:
  ans = A
else:
  ans = Z
ans1 = Y*A + ans
print(ans1)