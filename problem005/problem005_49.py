import sys
import math

a = []
for line in sys.stdin:
    a.append(line)

for n in a:
    inl=n.split()
    num1=int(inl[0])
    check=1
    list=[]
    while check<=math.sqrt(num1):
        if num1%check==0:
            list.append(check)
            list.append(num1/check)
        check+=1
    list.sort()
    list.reverse()
    num2=int(inl[1])
    for i in list:
        if num2%i==0:
            gud=i
            break
    lcm=num1*num2/gud
    print gud,lcm