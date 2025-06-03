h,n = map(int,input().split())
L = list(map(int,input().split()))
L.sort(reverse = True)
cnt = 0
for i in range(n):
    cnt  += L[i]
    if cnt >= h:
        print("Yes")
        exit()
print("No")