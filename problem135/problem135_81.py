a,b = input().split()
#print(a,b)
A = int(a)
x,y = b.split('.')
B = int(x)*100+int(y)

print(int(A*B)//100)