h,a = [int(i) for i in input().split()]

cont=0

while h > 0:
    h-=a
    cont+=1
print(cont)
