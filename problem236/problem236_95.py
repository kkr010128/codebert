H = int(input())
W = int(input())
N = int(input())
A = H if H > W else W
if N%A == 0:
    print(N//A)
else:
    print(N//A+1)