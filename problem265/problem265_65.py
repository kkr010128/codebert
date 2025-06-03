from math import ceil
n=int(input())
flag=True
xceil=ceil(n/1.08)
xfloor=int(n/1.08)
for i in range(xfloor,xceil+1):
    if int(i*1.08)==n:
        print(i)
        flag=False
        break
if flag:
    print(":(")