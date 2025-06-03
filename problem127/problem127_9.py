M,N = map(int,input().rstrip().split(" "))
ans=False
for a in range(M + 1):
    b=M-a
    if 2 * a + 4 * b == N:
        ans=True
if ans:
    print("Yes")
else:
    print("No")