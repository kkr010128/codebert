s=input()
n=int(input())
a=[input() for _ in range(n)]

front=True
f=""
b=""

for q in a:
    if q=="1":front=not front;continue
    l=q.split()
    if l[1]=="1":
        if front:f=l[2]+f
        else:b=b+l[2]
    if l[1]=="2":
        if front:b=b+l[2]
        else:f=l[2]+f

print(f+s+b if front else (f+s+b)[::-1])