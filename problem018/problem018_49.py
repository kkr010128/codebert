s=list(input().split())
a=[]
for x in s:
    if x in ['+','-','*']:
        c,b=str(a.pop()),str(a.pop())
        b+=x+c
        a+=[int(eval(b))]
    else:a+=[int(x)]
print(a.pop())