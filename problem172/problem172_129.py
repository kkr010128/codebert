N = int(input())
tmp = 0
for i in range(3):
    amari = N%10
    N //= 10
    if amari == 7:
        print('Yes')
        tmp = 1
        break
if tmp != 1:
    print('No')
