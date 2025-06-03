#k = int(input())
#s = input()
#a, b = map(int, input().split())
#l = list(map(int, input().split()))
n,m = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)
re = m
for i in range(n):
    if (4*m*a[i] >= total):
        re = re -1
        if (re == 0):
            print("Yes")
            exit()
print("No")
