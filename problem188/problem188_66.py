def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

x,y,a,b,c=sep()
red=lis()
green=lis()
colorless=lis()
red.sort(reverse=True)
green.sort(reverse=True)
colorless.sort()
red=red[:x][::-1]
green=green[:y][::-1]
i=0
j=0
while(colorless):
    if j>=y and i>=x:
        break
    elif j<y and i>=x:
        if colorless[-1]>green[j]:
            green[j]=colorless[-1]
            colorless.pop()
            j+=1
        else:
            break
    elif i<x and j>=y:
        if colorless[-1]>red[i]:
            red[i]=colorless[-1]
            colorless.pop()
            i+=1
        else:
            break

    elif red[i]<=green[j]:
        if colorless[-1]>red[i]:
            red[i]=colorless[-1]
            colorless.pop()
            i+=1
        else:
            break
    else:
        if colorless[-1]>green[j]:
            green[j]=colorless[-1]
            colorless.pop()
            j+=1
        else:
            break
#print(red,green)
print(sum(red) + sum(green))



