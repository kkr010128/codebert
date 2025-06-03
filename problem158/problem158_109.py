k=int(input())
a,b = map(int,input().split())

while b>=a:

    if b%k==0:
        print('OK')
        break

    b-=1

if b<a:
    print('NG')