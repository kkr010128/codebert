n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i],b[i] = map(int,input().split())
a.sort()
b.sort()
if n % 2 == 1:
    print(b[n//2] - a[n//2] + 1)
else:
    front = n//2
    back = (n-1)//2
    print((b[front] + b[back] - (a[front] + a[back]) + 1))
