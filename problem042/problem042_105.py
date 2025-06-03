count = 1
while True:
    x = input().strip()
    if x == '0':
        break
    else:
        print('Case %s: %s' %(count, x))
        count = count + 1