a, b, k =map(int, input().split())

if k <= a:
    a = a-k
    b = b

elif a+b <= k:
    a = 0
    b = 0

else:
    b = a+b-k
    a = 0
    

print(a, b)
