n,m = [int(x) for x in input().split()]
a=[]
b=[]

for i in range(n): a.append([int(x) for x in input().split()])
for j in range(m): b.append(int(input()))
for a_row in a:
    print(sum([x*y for x,y in zip(a_row,b)]))
