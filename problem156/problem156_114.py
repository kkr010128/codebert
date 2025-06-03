x = int(input())

l = [i**5 for i in range(1000)]

for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]-l[i]==x:
            print(int(l[j]**(1/5)),int(l[i]**(1/5)))
            exit()
        if l[j]+l[i]==x:
            print(int(l[j]**(1/5)),-int(l[i]**(1/5)))
            exit()
print('Not found')