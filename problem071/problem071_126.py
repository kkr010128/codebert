S = input()
ss = S[::-1]
if ss[0]=='s':
    S += 'es'
else:
    S += 's'

print(S)
