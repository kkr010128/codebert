l = input().split()

'''
a = int(l[0])
b = int(l[1])
'''
#存在していないインデックスは出せない
l = list(map(int,l))

a = l[0]*l[1]
b = 2*(l[0]+l[1])

print(a,b)
