n = int(input())
al = list(map(int, input().split()))

flg = True
for a in al:
    if a%2 == 0:
        if a%3 == 0 or a%5 == 0:
            continue
        else:
            flg = False
            break

if flg:
    print('APPROVED')
else:
    print('DENIED')