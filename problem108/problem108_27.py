N = int(input())
if N%1000==0:
    q = N//1000-1
else:
    q = N//1000
ans = 1000*(q+1)-N
print(ans)
