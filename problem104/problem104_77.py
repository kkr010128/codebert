l,r,n = map(int,input().split(" "))
count = 0
for i in range(l,r+1):
    if i % n == 0:
        count += 1
print(count)
