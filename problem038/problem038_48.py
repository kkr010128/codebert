a,b=map(int, input().split())
if a > b:
    s = '>'
elif a<b:
    s = '<'
else:
    s = '=='
print('a {} b'.format(s))

