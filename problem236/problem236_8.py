H = int(input())
W = int(input())
N = int(input())

x = H if H>W else W
x2 = 0 if N%x==0 else 1

print(N//x + x2)
