n = int(input())
a, b = input().split()
a,b = int(a) , int(b)
flag = True
for i in range(1000,1,-1):
    if i%n==0:
        if a<=i and i<=b:
            print('OK')
            flag = False
            break
if flag:
    print('NG')

