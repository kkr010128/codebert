list=[0 for i in range(10**4+1)]
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            var=x**2 +y**2 +z**2 +x*y +y*z +z*x
            if var<=10**4:
                list[var]+=1
            
n=int(input())
for i in range(1,n+1):
    print(list[i])