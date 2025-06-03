N=int(input())
right=0
left=0
for i in range(N):
    a,b=input().split()
    if a>b:
        left+=3
    elif a<b:
        right+=3
    else:
        left+=1
        right+=1
print(f"{left} {right}")
