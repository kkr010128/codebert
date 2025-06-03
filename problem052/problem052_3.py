def inc3(i):
    if i - (i // 10)*10 == 3:
        return(True)
    elif i//10==0:
        return(False)
    else:    
        return(inc3(i//10))

n = int(input())
for i in range(1,n+1):
    if i%3==0 or inc3(i):
        print(" " + str(i),end="")
print()