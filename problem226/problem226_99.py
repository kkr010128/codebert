h,n=map(int,input().split())

A=list(map(int,input().split()))

attack=0
for i in range(n):
    attack+=A[i]
    
if attack>=h:
    print("Yes")
else:
    print("No")