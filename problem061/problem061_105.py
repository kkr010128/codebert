x=[(i) for i in input().split()]
for i in range(len(x)-1):
    print(x[i].swapcase(),"",end="")
print(x[len(x)-1].swapcase())