s = input()
f = False
chk = ''
for i in range(5):
    chk += 'hi'
    if s == chk:
        print('Yes')
        f = True
        break
if not f:
    print('No')