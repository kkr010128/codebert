k = int(input())
a = 7%k
if a == 0:
    print(1)
    exit()
for i in range(1,k+1):
    a = (10*a + 7)%k
    if a == 0:
        print(i+1)
        exit()
print(-1)