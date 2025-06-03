X=int(input())
ans=100
count=0
while ans<X:
    ans=ans+(ans//100)
    count+=1
print(count)