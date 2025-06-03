S = list(input())
if S[-1] == 's':
    S.append('e')
    S.append('s')
else:
    S.append('s')
strS = ''.join(S)
print(strS)