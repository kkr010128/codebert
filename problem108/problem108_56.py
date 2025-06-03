i = int(input())
k = 1000
while k < i:
    k += 1000
    
if k > i:
    print(k - i)
elif k == i:
    print(0)