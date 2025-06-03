#A - Table Tennis Training
N,A,B = map(int,input().split())
if abs(A-B)%2 == 0:
    ans = abs(A-B)//2
else:
    a = min(A-1,N-B)
    ans = a + 1 + (B-A-1)//2
print(ans)