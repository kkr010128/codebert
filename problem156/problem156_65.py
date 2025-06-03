x = int(input())
a = [0]*1000
for i in range(1000):
    tmp = i**5
    a[i] = tmp
for i in range(1000):
    for j in range(1000):
        if((a[i]-x) == (a[j])):
            print(i,j)
            exit()
        elif(x-a[i]==a[j]):
            print(i,-j)
            exit()
