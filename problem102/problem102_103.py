n = list(map(int,input().split()))
a = list(map(int,input().split()))

for i in range(n[1],n[0]):
    if a[i-n[1]] < a[i]:
        print("Yes")
    else:
        print("No")