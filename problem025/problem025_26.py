n=int(input())
A=[int(x) for x in input().split()]
q=int(input())
m=[int(x) for x in input().split()]

A_sum = []
for bit in range(1,2**n):
    a_sum = 0
    for i in range(n):
        if bin((bit>>i) & 0b1) == '0b1':
            a_sum += A[i]
    A_sum.append(a_sum)
            
for mi in m:
    if mi in A_sum:
        print('yes')
    else:
        print('no')
