a,b = map(int,input().split())
num_a = ''
num_b = ''
lst = []
for i in range(b):
    num_a += str(a)
for i in range(a):
    num_b += str(b)
lst.append(num_a)
lst.append(num_b)
lst.sort()
print(lst[0])
