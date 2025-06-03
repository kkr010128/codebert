n =  int(input())
A = list(map(int, input().split()))

l = []
for a in A:
    if a % 2 == 0:
        l.append(a)

if all([i % 3 ==0 or i % 5 ==0 for i in l]):
    print('APPROVED')
else:
    print('DENIED')