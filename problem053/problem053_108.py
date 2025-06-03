n = int(input())
Nlist = input().split()
for i in range(n-1):
    print(Nlist[n-i-1],end=" ")
print(Nlist[0])