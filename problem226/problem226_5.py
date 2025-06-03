H,N=map(int,input().split())
A=input()
list_A=A.split()
waza=0
for i in range(0,N):
    waza=waza+int(list_A[i])
if waza>=H:
    print("Yes")
else:
    print("No")