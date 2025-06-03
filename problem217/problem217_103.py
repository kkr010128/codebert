import sys
n=int(input())
a=list(map(int,input().split()))
b=a[:]

for i in range(len(a)):
    if a[i]%2!=0:
        b.remove(a[i])

for i in b:
    if i%3!=0:
        if i%5!=0:
            print('DENIED')
            sys.exit()
            
print('APPROVED')