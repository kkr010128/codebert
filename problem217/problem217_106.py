N = int(input())
lst = list(map(int, input().split()))
c = True
for i in lst:
    if i%2 ==0:
        if i%3 != 0 and i%5 != 0:
            c = False
            break
    
if c:
    print('APPROVED')
else:
    print('DENIED')