x = int(input())
sosu = [int(i) for i in range(2*x)]
sosu[1] = 0
for i in range(2,x):
    if sosu[i]!=0:
        j = 2
        while i * j < 2*x:
            sosu[i*j]=0
            j += 1
#print(sosu[x])
while sosu[x]==0:
    x += 1
print(x)
