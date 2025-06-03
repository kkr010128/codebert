l= list(input().split())
a,b = map(int,input().split())
u = input()
if u == l[0]:
    a -= 1
else:
    b -= 1
print(a,b)