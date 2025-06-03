n = str(input())
if n[len(n)-1] in '24579':
    print('hon')
elif n[len(n)-1] in '0168':
    print('pon')
else:
    print('bon')