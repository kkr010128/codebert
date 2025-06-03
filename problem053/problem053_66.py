a=[]
n = int(input())

s = input().rstrip().split(" ")

for i in range(n):
    a.append(int(s[i]))
a=a[::-1]
for i in range(n-1):
    print(a[i],end=' ' )
print(a[n-1])