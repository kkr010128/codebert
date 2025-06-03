a,b,c = map(int,input().split())

if a + b + c >= 22:
    print('bust')
if a + b + c <= 21:
    print('win')
