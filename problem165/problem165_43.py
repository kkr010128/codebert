n=int(input())
l =[]
for i in range(n):
    s =input()
    l.append(s)

l = set(l)
print(len(l))