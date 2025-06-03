a = list(map(int, input().split()))
a.sort()

while a[0] > 0:
    b = a[1]%a[0]
    a[1] = a[0]
    a[0] = b
    
print(a[1])