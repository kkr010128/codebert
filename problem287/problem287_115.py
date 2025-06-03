n = int(input())
#lis = list(map(int,input().split()))

for i in range(1,10):
    q = n // i
    r = n % i
    if r == 0 and q < 10:
        print("Yes")
        exit()

print("No")