A,B = map(int,(input().split()))

l = 0
if A > B: 
    l = A
    s = B
else:
    l = B
    s = A

for i in range(1,10**10):
    if (l*i)%s == 0:
        print(l*i)
        exit()
    else:
        continue