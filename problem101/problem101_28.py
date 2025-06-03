a = list(map(int, input().split()))
n = int(input())

for i in range(n):
    if a[0] >= a[1]:
        a[1] *= 2
    elif a[1] >= a[2]:
        a[2] *= 2
    
if a[0] < a[1] < a[2]:
    print("Yes")
else:
    print("No")   

