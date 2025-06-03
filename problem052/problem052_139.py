n = int(input())
ret = ''

for i in range(1,n+1):
    str = repr(i)
    if (i % 3 == 0): ret += ' ' + repr(i)
    elif ('3' in str): ret += ' ' + repr(i)
    
print(ret)