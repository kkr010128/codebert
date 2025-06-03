number=list(map(int,input().split()))
for i in range(1,10):
    if number.count(i)==2:
        print("Yes")
        exit(0)
print("No")