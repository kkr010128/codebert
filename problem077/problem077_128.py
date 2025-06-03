a,b,c,d = map(int,input().split())
li = list()
li.append(a * c)
li.append(a * d)
li.append(b * c)
li.append(b * d)

print(max(li))