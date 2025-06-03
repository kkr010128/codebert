n = int(input())
a = [list(input().split()) for i in range(n)]
x = input()
#print(a)

res = 0
start = 0
for i in range(n):
    if a[i][0] == x:
        start = i+1
for i in range(start,n):
    res += int(a[i][1])
print(res)