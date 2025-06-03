n,m = map(int,input().split())
a = list(map(int,input().split()))
b = sum(a)/(4*m)
cnt = 0
for i in a:
    if b <= i:
        cnt += 1
        if cnt >= m:
            print("Yes")
            exit()
print("No")