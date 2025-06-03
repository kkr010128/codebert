n = int(input())
a = list(map(int,input().split()))
a.reverse()
for i in range(n-1):
    print(a[i],end = " ")
print(a[n-1])