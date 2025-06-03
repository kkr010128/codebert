line = list(map(int,input().split()))
if line[0]==line[1]: op = '=='
if line[0]>line[1]: op = '>'
if line[0]<line[1]: op = '<'
print('a {op} b'.format(op=op))