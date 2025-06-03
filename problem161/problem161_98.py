A,B,N=map(int,input().split())

max = 0
if B - 1 >= N:
    i = N
else:
    i = B - 1
ans = A*i//B - A*(i//B)

print(ans)
