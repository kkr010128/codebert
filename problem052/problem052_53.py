n = int(input())
for i in range(n):
    if (i+1)%3==0:
        print(" "+str(i+1), end="")
    else:
        x = i+1
        while(x>0):
            if x%10==3:
                print(" "+str(i+1), end="")
                break
            else:
                x = x//10
print("")