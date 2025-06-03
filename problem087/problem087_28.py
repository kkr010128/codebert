n = list(input())

n1 = [int(i) for i in n]

sum = 0
for i in n1:
    sum += i

if sum % 9 == 0:
    print('Yes')

else:
    print('No')