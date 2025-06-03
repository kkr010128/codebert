a = int(input())
x = input()
y = x.split(' ')
c =[]
for i in range(a):
    c.append(y[(a-1)-i])
b = ' '.join(c)
print(b)