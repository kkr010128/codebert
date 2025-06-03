n=map(str,raw_input().split())
a=[]
ai=0
for i in n:
    if i=="+" :
        a.append(a[ai-1]+a[ai-2])
        a.pop(ai-1);a.pop(ai-2)
        ai-=1
    elif i=="-":
        a.append(a[ai-2]-a[ai-1])
        a.pop(ai-1);a.pop(ai-2)
        ai-=1
    elif i=="*":
        a.append(a[ai-1]*a[ai-2])
        a.pop(ai-1);a.pop(ai-2)
        ai-=1
    else:
        a.append(int(i))
        ai+=1
print(a[0])