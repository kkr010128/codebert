L,R,d = list(map(int, input().split()))
count = 0
for i in range(L,R+1):
    count += (i%d == 0)
print(count)