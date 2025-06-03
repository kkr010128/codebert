n = int(input())
a0 = 1
a1 = 1

#print(a0, a1, end='')
if n == 0 or n == 1:
    a2 = 1

else:
    for i in range(n-1):
        a2 = a0 + a1
        a0 = a1
        a1 = a2
    #print('',a2,end='')
print(a2)
