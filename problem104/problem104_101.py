L,R,d = map(int,input().split())
A = 0
for _ in range(L,R+1):
    if _ %d == 0:
        A += 1
print(A)