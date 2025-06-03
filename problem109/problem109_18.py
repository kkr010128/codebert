n=int(input())
S=[]
for i in range(n):
    S.append(input())

print('AC', 'x', S.count('AC'))
print('WA', 'x', S.count('WA'))
print('TLE', 'x', S.count('TLE'))
print('RE', 'x', S.count('RE'))
