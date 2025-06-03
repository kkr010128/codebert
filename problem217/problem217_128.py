N = int(input())
A = list(map(int, input().split()))
count = 0
sat = 0
for a in A:
    if a % 2 == 0:
        count += 1
        if a % 3 == 0 or a % 5 ==0:
            sat += 1
if count == sat:
    print('APPROVED')
else:
    print('DENIED')