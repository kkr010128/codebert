a,b,c,d = map(int, input().split())
z = 'BATTLE'
while z == 'BATTLE':
    c -= b
    if c <= 0:
        z = 'Yes'
        break
    a -= d
    if a <= 0:
        z ='No'
        break
print(z)