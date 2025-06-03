n = int(input())
a = [i for i in range(1,n+1) if (i%3==0 or "3" in list(str(i)))]
print(" ",end="")
print(*a,sep=" ")
