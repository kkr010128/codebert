x = input()
if x[-1] in 'sS':
    x += 'es'
else:
    x += 's'
    
print(x)