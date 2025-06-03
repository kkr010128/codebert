N = int(input())
A = list(map(int,input().split()))
B = len([i for i in A if i % 2==0])
count = 0
for i in A:
    if i % 2 !=0:
        continue
    elif i % 3 ==0 or i % 5==0:
        count  +=1
if count == B:
    print('APPROVED')
else:
    print('DENIED')
